from .data import *
from .forms import *
from .function import *
from .models import *
from . import models
from django.shortcuts import render, redirect
from django.contrib import messages
from math import *
from urllib.request import urlopen
from discord_webhook import DiscordWebhook, DiscordEmbed
from django.http import HttpResponse, HttpResponseRedirect
from http.cookies import CookieError
from datetime import timedelta, datetime
import json
import os
import sys
import traceback

# app_version = os.environ.get('APP_VERSION')
lang = ["English","Francais","Deutsch","Russian","Española"]
missing_data = []
WEBHOOK_URL = "https://discord.com/api/webhooks/#########/#############################################"
WEBHOOK_URL2 = "https://discord.com/api/webhooks/#########/#############################################"

def menu(request):
	cookie_result = checkCookie(request.COOKIES)
	darkmode = checkTheme_Request(request,cookie_result)
	return render(request, 'menu.html', {"darkmode": darkmode, "header_msg": "Menu Archero Wiki", 'lang':lang, "sidebarContent":SidebarContent})

def maze(request):
	cookie_result = checkCookie(request.COOKIES)
	darkmode = checkTheme_Request(request,cookie_result)
	with urlopen("https://config-archero.habby.mobi/data/config/MazeConfig.json") as url:
		data_json = json.load(url)
	return render(request, 'wiki/get_maze.html', {"data_json":data_json, "darkmode": darkmode, "header_msg": "maze","lang":lang, "sidebarContent":SidebarContent})


def csrf_failure(request, reason=""):
	cookie_value = checkCookie(request.COOKIES)
	try:
		ingame_id_cookie = list(cookie_value.values())[0]
		ingame_name_cookie = list(cookie_value.keys())[0]
		if ingame_id_cookie == "0-000000" and ingame_name_cookie == "visitor":
			profil = "no"
			public_id =''
		else:
			profil = "yes"
			user_stats = models.user.objects.get(ingame_id=ingame_id_cookie)
			public_id = user_stats.public_id
	except:
		profil = "no"
		public_id =''
	darkmode = checkTheme_Request(request,cookie_value)
	return render(request,'base/csrf_failure.html', {"darkmode": darkmode, "header_msg": "CSRF FAILURE","lang":lang, "profil":profil, "public_id":public_id, "sidebarContent":SidebarContent})


def login(request):
	cookie_value = checkCookie(request.COOKIES)
	darkmode = checkTheme_Request(request,cookie_value)
	if (len(cookie_value) >= 1 and "visitor" not in list(cookie_value)):
		username = list(cookie_value.keys())[0]
		send_webhook(f'{cookie_value} tried to access Login but was redirected to Home')
		messages.warning(request, f"You cannot go to Login : {username}")
		return HttpResponseRedirect("/")
	else:
		return render(request, "login.html", {"darkmode":darkmode, "sidebarContent":SidebarContent})

def login_processing(request, username_raw, id_raw):
	username_legal = checkIllegalKey(username_raw)
	response = redirect("/")
	boolCheck = checkUsernameCredentials(username_raw,id_raw)
	if boolCheck[1] == "visitor" and boolCheck[0]:
		response.set_cookie(key="visitor", value="0-000000", httponly=True, path='/')
	elif boolCheck[1] != 'visitor' and boolCheck[2] != '0-000000' and boolCheck[0]:
		response.delete_cookie('visitor', path='/')
		expires = datetime.now() + timedelta(days=365)
		try:
			response.set_cookie(key=boolCheck[1], value=boolCheck[2], expires=expires, httponly=True, samesite="Strict")
		except CookieError as e:
			send_webhook(f"<@382930544385851392> : {e}")
			messages.error(request, f'Login Failed (forbidden character "{username_legal}")')
			return response
		messages.success(request, f'Successful Login ({boolCheck[1]})')
		send_embed(boolCheck[1],"Successful Login",description_embed=f"",field_name=f"login/processing/{username_raw}/{id_raw}/",field_value=f"Credentials : `{boolCheck[1]}`|`{boolCheck[2]}`",e_color="32ec08",request=request, alert=False)
	else:
		messages.error(request, f'Login Failed : {boolCheck[3]}')
		send_embed(boolCheck[1],"Login Failed",description_embed=boolCheck[3],field_name=f"login/processing/{username_raw}/{id_raw}/",field_value=f"Credentials : `{boolCheck[1]}`|`{boolCheck[2]}`",e_color="d50400",request=request, alert=True)
	return response

def wiki_theorycrafting(request):
	cookie_result = checkCookie(request.COOKIES)
	darkmode = checkTheme_Request(request,cookie_result)
	return render(request, "wiki/theorycraft.html", {"darkmode": darkmode, "header_msg": "TheoryCrafting","lang":lang, "sidebarContent":SidebarContent, "TheoryCraftingContent":TheoryCraftingContent})

def item_description(request, item=None):
	cookie_result = checkCookie(request.COOKIES)
	darkmode = checkTheme_Request(request,cookie_result)
	ctx = {
		"darkmode": darkmode,
		"header_msg": "Item Description",
		"lang":lang,
		"item":"no",
		"sidebarContent":SidebarContent,
		"ItemData":ItemData
	}
	if item is None:
		item = "Brave_Bow"
	else:
		ctx.update({"item":"yes"})
	try:
		item_data = ItemData[str(item).replace('_',' ')]
		ctx.update({
			"name":str(item).replace('_',' '),
			"item_data":item_data,
			"url_cpy":request.build_absolute_uri(),
		})
	except Exception as e:
		messages.warning(request, message=f"{e} isn't an item")
	return render(request, "wiki/item_description.html", ctx)


def skill_description(request, skill=None):
	cookie_result = checkCookie(request.COOKIES)
	darkmode = checkTheme_Request(request,cookie_result)
	ctx = {
		"darkmode": darkmode,
		"header_msg": "Skill Description",
		"lang":lang,
		"skill":"no",
		"sidebarContent":SidebarContent,
		"SkillData":SkillData
	}
	if skill is None:
		skill = "Bouncy_Wall"
	else:
		ctx.update({"skill":"yes"})
	try:
		skill_name = skill.replace("_"," ")
		skill_data = SkillData[skill_name]
		image_skill = f"image/skill/{str(skill).lower().replace(' - ', '_').replace(' ', '_').replace('one-eyed', 'one_eyed')}.png"
		url_cpy = request.build_absolute_uri()
		ctx.update({
			"name":skill_name,
			"skill_data": skill_data,
			"image_skill":image_skill,
			"url_cpy":url_cpy,
		})
	except Exception as e:
		messages.warning(request, message=f"{e} isn't an skill")
	return render(request, "wiki/skill_description.html", ctx)

def heros_description(request, hero=None):
	cookie_result = checkCookie(request.COOKIES)
	darkmode = checkTheme_Request(request,cookie_result)
	ctx = {
		"darkmode": darkmode,
		"header_msg": "Heroes Description",
		"lang":lang,
		"hero":"no", ## keep this for the meta tag
		"sidebarContent":SidebarContent,
		"HeroData":HeroData
	}
	if hero is None:
		hero = "Atreus"
	else:
		ctx.update({"hero":"yes"})
	try:
		hero_data = HeroData[hero]
		ctx.update({
			"name_hero": hero,
			"hero_data": hero_data,
			"hero_image": f'image/hero_icon/icon_{str(hero)}.png',
			"url_cpy": request.build_absolute_uri(),
		})
	except Exception as e:
		messages.warning(request, message=f"{e} isn't a hero")
	return render(request, "wiki/heros_description.html",ctx)

def upgrade_cost(request,cost_type:str="None",lvl1:int=999,lvl2:int=999,rank:str="None"):
	cookie_result = checkCookie(request.COOKIES)
	darkmode = checkTheme_Request(request,cookie_result)
	all_rank = ["A","S","SS"]
	content = ""
	ctx = {
		"darkmode": darkmode,
		"header_msg": "Upgrade Cost",
		"lang":lang,
		"cost_type":cost_type,
		"lvl1":lvl1,
		"lvl2":lvl2,
		"rank":rank,
		"sidebarContent":SidebarContent
	}
	if cost_type == "items":
		max_lvl = 170
		if (0 <= lvl1 <= max_lvl) and (0 <= lvl2 <= max_lvl):
			if lvl1 > lvl2:
				temp = lvl1
				lvl1 = lvl2
				lvl2 = temp
			price = calculatePrice(lvl1,lvl2,cost_type)
			content = {
				"eTitle": "Equipment Upgrade Cost",
				"eDescription": f"To upgrade equipment from level {lvl1} to {lvl2}",
				"eImage": "/static/image/wiki-image/Cost_Item.png",
				"eField1": f'{int(price[0]):,}',
				"eField2": f'{int(price[1]):,}',
				"currency1": ['Gold :','gold'],
				"currency2": ['Scrolls :','scroll'],
			}
		else:
			messages.error(request, message=f"The levels need to be between 0 and {max_lvl}")
			return HttpResponseRedirect(f"/wiki/upgrade/{cost_type}/1/2/")
	elif cost_type == "heroes":
		if lvl1 <= lvl2 and (0 <= lvl1 <= 119) and (1 <= lvl2 <= 120):
			price = calculatePrice(lvl1,lvl2,cost_type)
			content = {
				"eTitle": "Heroes Upgrade Cost",
				"eDescription": f"To upgrade heroes from level {lvl1} to {lvl2}",
				"eImage": "/static/image/wiki-image/Cost_Heroes.png",
				"eField1": f'{int(price[0]):,}',
				"eField2": f'{int(price[1]):,}',
				"currency1": ['Gold :','gold'],
				"currency2": ['Sapphire :','sapphire'],
			}
		else:
			messages.error(request, message="The levels need to be between 0 and 120")
			return HttpResponseRedirect(f"/wiki/upgrade/{cost_type}/1/2/")
	elif cost_type == "talents":
		if lvl1 <= lvl2 and (0 <= lvl1 <= 205) and (1 <= lvl2 <= 206):
			price = calculatePrice(lvl1,lvl2,cost_type)
			content = {
				"eTitle": "Talents Upgrade Cost",
				"eDescription": f"To upgrade talents from level {lvl1} to {lvl2}",
				"eImage": "/static/image/wiki-image/Cost_Talent.png",
				"eField1": f'{int(price):,}',
				"eField2": f'<br>',
				"currency1": ['Gold :','gold'],
				"currency2": ['',''],
			}
		else:
			messages.error(request, message="The levels need to be between 0 and 206")
			return HttpResponseRedirect(f"/wiki/upgrade/{cost_type}/1/2/")
	elif cost_type == "dragons":
		if lvl1 <= lvl2 and (0 <= lvl1 <= 119) and (1 <= lvl2 <= 120):
			if rank in all_rank:
				price = calculatePrice(lvl1,lvl2,cost_type,rank)
				content = {
					"eTitle": "Dragon Upgrade Cost",
					"eDescription": f"To upgrade dragons from level {lvl1} to {lvl2}",
					"eImage": "/static/image/wiki-image/Cost_Dragon" + str(rank).upper() + ".png",
					"eField1": f'{int(price[0]):,}',
					"eField2": f'{int(price[1]):,}',
					"currency1": ['Gold :','gold'],
					"currency2": ['Magestones :','magestone'],
				}
			else:
				messages.error(request, message="The rank need to be whether A, S or SS")
				return HttpResponseRedirect(f"/wiki/upgrade/{cost_type}/{lvl1}/{lvl2}/A/")
		else:
			messages.error(request, message="The levels need to be between 0 and 120")
			return HttpResponseRedirect(f"/wiki/upgrade/{cost_type}/1/2/{rank}/")
	elif cost_type == "relics":
		if lvl1 <= lvl2 and (0 <= lvl1 <= 29) and (1 <= lvl2 <= 30):
			if rank in all_rank:
				price = calculatePrice(lvl1,lvl2,cost_type,rank)
				content = {
					"eTitle": "Relics Upgrade Cost",
					"eDescription": f"To upgrade relics from level {lvl1} to {lvl2}",
					"eImage": "/static/image/wiki-image/Cost_Relics" + str(rank).upper() + ".png",
					"eField1": f'{int(price[0]):,}',
					"eField2": f'{int(price[1]):,}',
					"currency1": ['Gold :','gold'],
					"currency2": ['Starlight :','starlight'],
				}
			else:
				messages.error(request, message="The rank need to be whether A, S or SS")
				return HttpResponseRedirect(f"/wiki/upgrade/{cost_type}/{lvl1}/{lvl2}/A/")
		else:
			messages.error(request, message="The levels need to be between 0 and 30")
			return HttpResponseRedirect(f"/wiki/upgrade/{cost_type}/1/2/{rank}/")
	ctx.update({"content":content})
	return render(request, "wiki/upgrade_cost.html", ctx)


def ghssetGrid(request):
	cookie_result = checkCookie(request.COOKIES)
	darkmode = checkTheme_Request(request,cookie_result)
	ctx = {
		'darkmode':darkmode,
		"header_msg": "Google Sheet Wiki",
		"lang":lang,
		"GsheetData":GsheetData,
		"sidebarContent":SidebarContent
	}
	return render(request, "wiki/gsheet.html", ctx)

def promocode(request):
	cookie_result = checkCookie(request.COOKIES)
	darkmode = checkTheme_Request(request,cookie_result)
	all_active_code = []
	promo_codes = models.promo_code.objects.all().filter(is_active=True)
	for i in promo_codes:
		expireDate = i.expire
		if i.expire == None:
			expireDate = ""
		r1 = [i.reward_1_amount,i.reward_1_type]
		r2 = [i.reward_2_amount,i.reward_2_type]
		r3 = [i.reward_3_amount,i.reward_3_type]
		r4 = [i.reward_4_amount,i.reward_4_type]
		if str(r1[1]) != "none":
			result = [i.code,expireDate,[r1]]
			if str(r2[1]) != "none":
				result = [i.code,expireDate,[r1,r2]]
				if str(r3[1]) != "none":
					result = [i.code,expireDate,[r1,r2,r3]]
					if str(r4[1]) != "none":
						result = [i.code,expireDate,[r1,r2,r3,r4]]
			all_active_code.append(result)
	ctx = {
		"darkmode": darkmode,
		"header_msg": "Promo Code",
		"lang":lang,
		"promo_code":all_active_code,
		"len_promo":len(all_active_code),
		"sidebarContent":SidebarContent
	}
	return render(request, "wiki/promo-code.html", ctx)


def damage(request):
	cookie_value = checkCookie(request.COOKIES)
	darkmode = checkTheme_Request(request,cookie_value)
	user_stats = ""
	if len(cookie_value) != 0:
		ingame_id_cookie = list(cookie_value.values())[0]
		ingame_name_cookie = list(cookie_value.keys())[0]
		if ingame_id_cookie == "0-000000" and ingame_name_cookie == "visitor":
			selfHasProfil = "login"
		else:
			try:
				user_stats = models.user.objects.get(ingame_id=ingame_id_cookie)
				selfHasProfil = "yes"
			except:
				selfHasProfil = "no"
	else:
		selfHasProfil = "login"
	chapter_1_to_21 =  models.user.objects.get(ingame_id="0-000001").public_id
	chapter_22_to_34 = models.user.objects.get(ingame_id="0-000002").public_id
	chapter_34_to_42 = models.user.objects.get(ingame_id="0-000003").public_id
	chapter_ch42 =  models.user.objects.get(ingame_id="0-000004").public_id
	ctx = {
		"darkmode": darkmode,
		"header_msg": "Damage Help",
		"selfHasProfil":selfHasProfil,
		"selfStats":user_stats,
		"lang":lang,
		"chapter_1_to_21":chapter_1_to_21,
		"chapter_22_to_34":chapter_22_to_34,
		"chapter_34_to_42":chapter_34_to_42,
		"chapter_ch42":chapter_ch42,
		"sidebarContent":SidebarContent
		}
	return render(request, "wiki/damage.html", ctx)


def dmgCalc_processing(request,pbid):
	global missing_data
	user_stats = models.user.objects.get(public_id=pbid)
	stuff_table_stats = models.stuff_table.objects.get(user_profile=user_stats)
	hero_table_stats = models.hero_table.objects.get(user_profile=user_stats)
	talent_table_stats = models.talent_table.objects.get(user_profile=user_stats)
	skin_table_stats = models.skin_table.objects.get(user_profile=user_stats)
	altar_table_stats = models.altar_table.objects.get(user_profile=user_stats)
	jewel_level_table_stats = models.jewel_level_table.objects.get(user_profile=user_stats)
	egg_table_stats = models.egg_table.objects.get(user_profile=user_stats)
	egg_equipped_table_stats = models.egg_equipped_table.objects.get(user_profile=user_stats)
	dragon_table_stats = models.dragon_table.objects.get(user_profile=user_stats)
	runes_table_stats = models.runes_table.objects.get(user_profile=user_stats)
	reforge_table_stats = models.reforge_table.objects.get(user_profile=user_stats)
	refine_table_stats = models.refine_table.objects.get(user_profile=user_stats)
	medals_table_stats = models.medals_table.objects.get(user_profile=user_stats)
	relics_table_stats = models.relics_table.objects.get(user_profile=user_stats)
	weapon_skins_table_stats = models.weapon_skins_table.objects.get(user_profile=user_stats)

	atk_base_hero_choosen = user_stats.atk_base_stats_hero_choosen

	stuff_altar_ascension = altar_table_stats.stuff_altar_ascension
	heros_altar_ascension = altar_table_stats.heros_altar_ascension

	runes_power_attack_flat = runes_table_stats.power_attack_flat
	runes_power_attack_var = runes_table_stats.power_attack_var
	runes_courage_attack_flat = runes_table_stats.courage_attack_flat
	runes_courage_attack_var = runes_table_stats.courage_attack_var

	refine_weapon_atk = refine_table_stats.weapon_refine_atk
	refine_weapon_enhanced_equipment = int(refine_table_stats.weapon_refine_basic_stats)/100
	refine_armor_enhanced_equipment = int(refine_table_stats.armor_refine_basic_stats)/100
	refine_ring1_atk = refine_table_stats.ring1_refine_atk
	refine_ring1_enhanced_equipment = int(refine_table_stats.ring1_refine_basic_stats)/100
	refine_ring2_atk = refine_table_stats.ring2_refine_atk
	refine_ring2_enhanced_equipment = int(refine_table_stats.ring2_refine_basic_stats)/100
	refine_bracelet_atk = refine_table_stats.bracelet_refine_atk
	refine_bracelet_enhanced_equipment = int(refine_table_stats.bracelet_refine_basic_stats)/100
	refine_locket_enhanced_equipment = int(refine_table_stats.locket_refine_basic_stats)/100
	refine_book_enhanced_equipment = int(refine_table_stats.book_refine_basic_stats)/100

	brave_privileges_level = int(user_stats.brave_privileges_level)
	## Get Talents Stats
	talent_stats_dict = talent_table_stats.getTalentStats()
	## Get Altar Ascension Stats
	altar_stuff_ascension_atk = StuffAltarAscension[str(stuff_altar_ascension) + '_attack']
	altar_stuff_ascension_equipment_base = StuffAltarAscension[str(stuff_altar_ascension) + '_equipment_base']
	altar_heros_ascension_atk = HerosAltarAscension[str(heros_altar_ascension) + '_attack']
	altar_heros_ascension_heros_base = HerosAltarAscension[str(heros_altar_ascension) + '_heros_base']
	## Get Altar Stats 
	altar_stuff_atk = altar_table_stats.CalculAltar("stuff","attack")
	altar_hero_atk = altar_table_stats.CalculAltar("heros","attack") ##laissé le S (le nom du field prend un s)
	# Get All Heroes Stats
	hero_Atreus = hero_table_stats.HerosStatsRecup("Atreus")
	hero_Urasil = hero_table_stats.HerosStatsRecup("Urasil")
	hero_Phoren = hero_table_stats.HerosStatsRecup("Phoren")
	hero_Taranis = hero_table_stats.HerosStatsRecup("Taranis")
	hero_Helix = hero_table_stats.HerosStatsRecup("Helix") 
	hero_Meowgik = hero_table_stats.HerosStatsRecup("Meowgik")
	hero_Shari = hero_table_stats.HerosStatsRecup("Shari")
	hero_Ayana = hero_table_stats.HerosStatsRecup("Ayana")
	hero_Onir = hero_table_stats.HerosStatsRecup("Onir") 
	hero_Rolla = hero_table_stats.HerosStatsRecup("Rolla")
	hero_Bonnie = hero_table_stats.HerosStatsRecup("Bonnie")
	hero_Sylvan = hero_table_stats.HerosStatsRecup("Sylvan")
	hero_Shade = hero_table_stats.HerosStatsRecup("Shade") 
	hero_Ophelia = hero_table_stats.HerosStatsRecup("Ophelia")
	hero_Ryan = hero_table_stats.HerosStatsRecup("Ryan")
	hero_Lina = hero_table_stats.HerosStatsRecup("Lina")
	hero_Aquea = hero_table_stats.HerosStatsRecup("Aquea")
	hero_Shingen = hero_table_stats.HerosStatsRecup("Shingen") 
	hero_Gugu = hero_table_stats.HerosStatsRecup("Gugu")
	hero_Iris = hero_table_stats.HerosStatsRecup("Iris")
	hero_Blazo = hero_table_stats.HerosStatsRecup("Blazo")
	hero_Melinda = hero_table_stats.HerosStatsRecup("Melinda")
	hero_Elaine = hero_table_stats.HerosStatsRecup("Elaine")
	hero_Bobo = hero_table_stats.HerosStatsRecup("Bobo")
	hero_Stella = hero_table_stats.HerosStatsRecup("Stella")
	## Get Skin Atk and Hp
	skin_atk_boost = skin_table_stats.skin_attack
	## Get Passiv Stats From Type 1 Egg
	egg_green_bat_passiv = egg_table_stats.GetPassivEggStats1("green_bat", missing_data)
	egg_bomb_ghost_passiv = egg_table_stats.GetPassivEggStats1("bomb_ghost",missing_data)
	egg_piranha_passiv = egg_table_stats.GetPassivEggStats1("piranha",missing_data)
	## Get Passiv Stats From Type 2 Egg
	egg_skeleton_archer_passiv = egg_table_stats.GetPassivEggStats2("skeleton_archer",missing_data)
	egg_skeleton_soldier_passiv = egg_table_stats.GetPassivEggStats2("skeleton_soldier",missing_data)
	egg_fire_mage_passiv = egg_table_stats.GetPassivEggStats2("fire_mage",missing_data)
	egg_ice_mage_passiv = egg_table_stats.GetPassivEggStats2("ice_mage",missing_data)
	egg_flame_ghost_passiv = egg_table_stats.GetPassivEggStats2("flame_ghost",missing_data)
	egg_tornado_demon_passiv = egg_table_stats.GetPassivEggStats2("tornado_demon",missing_data)
	egg_skull_wizard_passiv = egg_table_stats.GetPassivEggStats2("skull_wizard",missing_data)
	egg_crazy_spider_passiv = egg_table_stats.GetPassivEggStats2("crazy_spider",missing_data)
	egg_fire_element_passiv = egg_table_stats.GetPassivEggStats2("fire_element",missing_data)
	egg_pea_shooter_passiv = egg_table_stats.GetPassivEggStats2("pea_shooter",missing_data)
	egg_shadow_assassin_passiv = egg_table_stats.GetPassivEggStats2("shadow_assassin",missing_data)
	egg_one_eyed_bat_passiv = egg_table_stats.GetPassivEggStats2("one_eyed_bat",missing_data)
	egg_scarlet_mage_passiv = egg_table_stats.GetPassivEggStats2("scarlet_mage",missing_data)
	egg_icefire_phantom_passiv = egg_table_stats.GetPassivEggStats2("icefire_phantom",missing_data)
	egg_purple_phantom_passiv = egg_table_stats.GetPassivEggStats2("purple_phantom",missing_data)
	egg_savage_spider_passiv = egg_table_stats.GetPassivEggStats2("savage_spider",missing_data)
	egg_flaming_bug_passiv = egg_table_stats.GetPassivEggStats2("flaming_bug",missing_data)
	egg_crimson_zombie_passiv = egg_table_stats.GetPassivEggStats2("crimson_zombie",missing_data)
	egg_elite_archer_passiv = egg_table_stats.GetPassivEggStats2("elite_archer",missing_data)
	## Get Passiv Stats From Type 3 Egg
	egg_arch_leader_passiv = egg_table_stats.GetPassivEggStats3("arch_leader",missing_data)
	egg_skeleton_king_passiv = egg_table_stats.GetPassivEggStats3("skeleton_king",missing_data)
	egg_crimson_witch_passiv = egg_table_stats.GetPassivEggStats3("crimson_witch",missing_data)
	egg_queen_bee_passiv = egg_table_stats.GetPassivEggStats3("queen_bee",missing_data)
	egg_ice_worm_passiv = egg_table_stats.GetPassivEggStats3("ice_worm",missing_data)
	egg_medusa_boss_passiv = egg_table_stats.GetPassivEggStats3("medusa_boss",missing_data)
	egg_ice_demon_passiv = egg_table_stats.GetPassivEggStats3("ice_demon",missing_data)
	egg_giant_owl_passiv = egg_table_stats.GetPassivEggStats3("giant_owl",missing_data)
	egg_fire_demon_passiv = egg_table_stats.GetPassivEggStats3("fire_demon",missing_data)
	egg_krab_boss_passiv = egg_table_stats.GetPassivEggStats3("krab_boss",missing_data)
	egg_desert_goliath_passiv = egg_table_stats.GetPassivEggStats3("desert_goliath",missing_data)
	egg_scythe_pharoah_passiv = egg_table_stats.GetPassivEggStats3("scythe_pharoah",missing_data)
	egg_infernal_demon_passiv = egg_table_stats.GetPassivEggStats3("infernal_demon",missing_data)
	egg_sinister_touch_passiv = egg_table_stats.GetPassivEggStats3("sinister_touch",missing_data)
	egg_fireworm_queen_passiv = egg_table_stats.GetPassivEggStats3("fireworm_queen",missing_data)
	# Get All Jewel's Stats
	stats_jewel_dict = jewel_level_table_stats.JewelStatsRecup()
	## Get Brave Privilege Stats
	brave_privileges_stats = BravePrivileges['level' + str(brave_privileges_level)]
	## Get Special Bonus Stats
	BonusSpe_jewel_weapon = jewel_level_table_stats.JewelSpeBonusStatsRecup('weapon',brave_privileges_stats['Weapon JSSSA'])
	BonusSpe_jewel_ring1 = jewel_level_table_stats.JewelSpeBonusStatsRecup('ring1',brave_privileges_stats['Ring JSSSA'])
	BonusSpe_jewel_bracelet = jewel_level_table_stats.JewelSpeBonusStatsRecup('bracelet',brave_privileges_stats['Bracelet JSSSA'])
	BonusSpe_jewel_book = jewel_level_table_stats.JewelSpeBonusStatsRecup('book',brave_privileges_stats['Spellbook JSSSA'])
	## DRAGON stats
	dragon_1_stats_dict = dragon_table_stats.DragonStatueStats("1")
	dragon_2_stats_dict = dragon_table_stats.DragonStatueStats("2")
	dragon_3_stats_dict = dragon_table_stats.DragonStatueStats("3")
	## Get All Stats of Equipped Egg
	activ_egg_stats = egg_equipped_table_stats.GetEggStats(missing_data)
	## Get Reforge Stats
	reforge_atk_power = reforge_table_stats.ReforgePowerCourage("power")
	reforge_atk_courage = reforge_table_stats.ReforgePowerCourage("courage")
	## Get Reforge Stats
	rune_courage_hero = runes_table_stats.CourageBoostHero(user_stats.choosen_hero)
	## Get Rune Line Stats
	rune_line_stats = runes_table_stats.getValueLine()
	## Get Weapon Skin Stats
	weapon_skin_stats = weapon_skins_table_stats.getWeaponSkinStats()
	## Get all Medals Stats
	medal_stats = medals_table_stats.medal_calc()
	## Get all Relics Stats
	relics_stats = relics_table_stats.relics_Stats()

############################################## CALCUL #######################################################
	egg_var_passiv_heros_power_up = int(egg_arch_leader_passiv[3]) + int(egg_medusa_boss_passiv[3]) + int(egg_fire_demon_passiv[3]) + int(egg_krab_boss_passiv[3]) + int(egg_skeleton_king_passiv[1]) + int(egg_skeleton_king_passiv[3]) + int(egg_desert_goliath_passiv[1]) + int(egg_desert_goliath_passiv[3]) + int(egg_ice_demon_passiv[1]) + int(egg_ice_demon_passiv[3]) + int(egg_fireworm_queen_passiv[3]) + int(egg_sinister_touch_passiv[1]) + int(egg_infernal_demon_passiv[3]) + int(egg_scythe_pharoah_passiv[3])
	egg_var_passiv_enhanced_equipment = int(egg_crimson_witch_passiv[3]) + int(egg_queen_bee_passiv[3]) + int(egg_ice_worm_passiv[1]) + int(egg_ice_worm_passiv[3]) + int(egg_giant_owl_passiv[1]) + int(egg_giant_owl_passiv[3]) + int(egg_infernal_demon_passiv[1]) + int(egg_sinister_touch_passiv[3])
	cumul_var_passiv_power_up_hero = (float(relics_stats['hero_base_stats_increased_var']) + float(medal_stats['hero_base_enhanced']) + float(talent_stats_dict['talents_hero_power_up']) + float(egg_var_passiv_heros_power_up) + float(altar_heros_ascension_heros_base))/100
	cumul_var_passiv_enhanced_equipment = (float(rune_line_stats['var_enhanced_eqpm']) + float(relics_stats['enhance_equipment_var']) + float(medal_stats['enhance_equipment']) + float(talent_stats_dict['talents_enhanced_equipment']) + float(egg_var_passiv_enhanced_equipment) + float(altar_stuff_ascension_equipment_base))/100+1
	
	## Get Stuff Stats
	stuff_activ_stats = stuff_table_stats.getStuffStats(cumul_var_passiv_enhanced_equipment,refine_weapon_enhanced_equipment,refine_armor_enhanced_equipment,refine_ring1_enhanced_equipment,refine_ring2_enhanced_equipment,refine_bracelet_enhanced_equipment,refine_locket_enhanced_equipment,refine_book_enhanced_equipment,weapon_skin_stats)
	
	cumul_talent_flat_passiv_atk = int(talent_stats_dict['talents_power'])
	cumul_runes_flat_passiv_atk = int(reforge_atk_power) + int(reforge_atk_courage) # + int(runes_power_attack_flat) + int(runes_courage_attack_flat)
	cumul_hero_flat_passiv_atk = int(hero_Atreus[5]) + int(hero_Urasil[0]) + int(hero_Phoren[6]) + int(hero_Helix[5]) + int(hero_Meowgik[0]) + int(hero_Ayana[6]) + int(hero_Rolla[0]) + int(hero_Bonnie[5]) + int(hero_Shade[6]) + int(hero_Ophelia[0]) + int(hero_Ophelia[2]) + int(hero_Lina[0]) + int(hero_Lina[5]) + int(hero_Aquea[5]) + int(hero_Iris[5]) + int(hero_Melinda[6]) + int(hero_Iris[1]) + int(hero_Blazo[1]) + int(hero_Stella[0])
	cumul_skin_flat_passiv_atk = int(skin_atk_boost)
	cumul_egg_flat_passiv_atk = int(egg_bomb_ghost_passiv[1]) + int(egg_green_bat_passiv[1]) + int(egg_piranha_passiv[1]) + int(egg_crazy_spider_passiv[1]) + int(egg_fire_mage_passiv[1]) + int(egg_skeleton_archer_passiv[1]) + int(egg_skeleton_soldier_passiv[1]) + int(egg_fire_element_passiv[1]) + int(egg_flame_ghost_passiv[1]) + int(egg_ice_mage_passiv[1]) + int(egg_pea_shooter_passiv[1]) + int(egg_shadow_assassin_passiv[1]) + int(egg_skull_wizard_passiv[1]) + int(egg_tornado_demon_passiv[1]) + int(egg_savage_spider_passiv[1]) + int(egg_flaming_bug_passiv[1]) + int(egg_one_eyed_bat_passiv[1]) + int(egg_elite_archer_passiv[1]) + int(egg_icefire_phantom_passiv[1]) + int(egg_purple_phantom_passiv[1]) + int(egg_scarlet_mage_passiv[1]) + int(egg_arch_leader_passiv[0]) + int(egg_crimson_witch_passiv[0]) + int(egg_medusa_boss_passiv[0]) + int(egg_ice_worm_passiv[0]) + int(egg_desert_goliath_passiv[0]) + int(egg_ice_demon_passiv[0]) + int(egg_fire_demon_passiv[1]) + int(egg_crimson_zombie_passiv[1]) + int(egg_scythe_pharoah_passiv[1]) + int(egg_infernal_demon_passiv[0]) + int(egg_fireworm_queen_passiv[0])
	cumul_altar_flat_passiv_atk = int(altar_stuff_atk) + int(altar_hero_atk)
	cumul_jewel_flat_activ_atk = int(stats_jewel_dict['attack_ruby']) + int(stats_jewel_dict['attack_kunzite']) + int(stats_jewel_dict['attack_tourmaline']) + int(BonusSpe_jewel_weapon[0]) + int(BonusSpe_jewel_weapon[4]) + int(BonusSpe_jewel_bracelet[0]) + int(BonusSpe_jewel_bracelet[2]) + int(BonusSpe_jewel_bracelet[4])
	cumul_old_flat_passiv_atk = int(cumul_runes_flat_passiv_atk) + int(cumul_talent_flat_passiv_atk) + int(cumul_hero_flat_passiv_atk) + int(cumul_skin_flat_passiv_atk) + int(cumul_egg_flat_passiv_atk)
	cumul_refine_flat_activ_atk =  int(refine_weapon_atk) + int(refine_ring1_atk) + int(refine_ring2_atk) + int(refine_bracelet_atk)
	cumul_dragon_flat_activ_atk = int(dragon_1_stats_dict["Attack"]) + int(dragon_2_stats_dict["Attack"]) + int(dragon_3_stats_dict["Attack"])
	cumul_stuff_flat_activ_atk = round(stuff_activ_stats['weapon_total'] + stuff_activ_stats['bracelet_total'])

	cumul_heros_var_passiv_atk = float(hero_Taranis[2]) + float(hero_Meowgik[2]) + float(hero_Ayana[2]) + float(hero_Rolla[2]) + float(hero_Sylvan[2]) + float(hero_Aquea[2]) + float(hero_Iris[2]) + float(hero_Bonnie[4]) + float(hero_Shade[7]) + float(hero_Melinda[7]) + float(hero_Bobo[1]) + float(hero_Bobo[4]) + float(hero_Stella[2])
	cumul_heros_var_activ_atk = float(hero_Onir[3]) + float(hero_Bonnie[3])
	cumul_altar_var_passiv_atk = float(altar_heros_ascension_atk) + float(altar_stuff_ascension_atk)
	cumul_privileges_var_passiv_atk = float(brave_privileges_stats['Attack Var'])
	cumul_jewel_var_activ_atk =  (float(BonusSpe_jewel_weapon[2]) + float(BonusSpe_jewel_ring1[5]) + float(BonusSpe_jewel_book[2]))/100
	cumul_stuff_var_activ_atk = (stuff_activ_stats['weapon_attack_var'] + stuff_activ_stats['bracelet_attack_var'] + stuff_activ_stats['ring1_atk_var'] + stuff_activ_stats['ring2_atk_var'])

	cumul_var_atk = (float(cumul_heros_var_passiv_atk) + float(cumul_heros_var_activ_atk) + float(cumul_altar_var_passiv_atk) + float(cumul_privileges_var_passiv_atk) + float(medal_stats['attack_var']) + float(relics_stats['attack_var']))/100
	global_stats_atk_flat = int(cumul_stuff_flat_activ_atk) + int(int(activ_egg_stats["Attack"])) + int(cumul_altar_flat_passiv_atk) + int(cumul_dragon_flat_activ_atk) + int(brave_privileges_stats['Attack Flat']) + int(medal_stats['attack']) + int(relics_stats['attack'])

	hero_atk_step = [
		int(user_stats.global_atk_save),
		int(cumul_old_flat_passiv_atk), # + int(runes_power_attack_flat) + int(runes_courage_attack_flat)
		float(cumul_var_atk), # float(runes_power_attack_var) + float(runes_courage_attack_var)
		## atk_base_hero_choosen
		int(atk_base_hero_choosen),
		float(cumul_var_passiv_power_up_hero),
		#global_stats_atk_flat
		int(global_stats_atk_flat), # + int(hero_base_modified_stats_atk) + cumul_all_bonus_passif_atk
		#global_stats_atk
		float(cumul_stuff_var_activ_atk),
		float(cumul_jewel_var_activ_atk),
		int(cumul_jewel_flat_activ_atk),
		int(cumul_refine_flat_activ_atk),
		int(runes_power_attack_flat),
		int(runes_courage_attack_flat),
		float(runes_power_attack_var),
		float(runes_courage_attack_var),
		float(rune_courage_hero['current_hero_atk_flat']),
		float(rune_courage_hero['current_hero_atk_var'])
	]

	if request.method == "GET":
		try:
			calc_user_dmg = models.dmg_calc_table.objects.get(user_profile=user_stats)
			calc_user_dmg.hero_atk = hero_atk_step
			calc_user_dmg.save()
			return HttpResponseRedirect(f"/wiki/damage-calculator/{pbid}/")
		except Exception:
			return HttpResponseRedirect(f"/stats/calc/{pbid}/2/")
	else :
		return HttpResponseRedirect("/wiki/damage-calculator/")


def damageCalc(request,pbid):
	cookie_result = checkCookie(request.COOKIES)
	darkmode = checkTheme_Request(request,cookie_result)
	try:
		user_stats = models.user.objects.get(public_id=pbid)
		calc_user_dmg = models.dmg_calc_table.objects.get(user_profile=user_stats.pk)
		runes_table_stats = models.runes_table.objects.get(user_profile=user_stats.pk)
	except:	
		return HttpResponseRedirect("/")
	ctx = {
		'darkmode':darkmode,
		"header_msg": "Damage Calc",
		"lang":lang,
		"sidebarContent":SidebarContent
	}
	if request.method == "GET":
		damage_calc_form = DamageCalculatorForm()
		resultCalcDamg = calc_user_dmg.calculDamage()
		ctx['averageDamage'] = resultCalcDamg['averageDamageAll']
		ctx['crit_dmg'] = calc_user_dmg.crit_dmg
		ctx['crit_rate'] = calc_user_dmg.crit_rate
		ctx["mob_ground_melee_damage"] = resultCalcDamg['mob_ground_melee_damage']
		ctx["mob_ground_range_damage"] = resultCalcDamg['mob_ground_range_damage']
		ctx["mob_airborne_melee_damage"] = resultCalcDamg['mob_airborne_melee_damage']
		ctx["mob_airborne_range_damage"] = resultCalcDamg['mob_airborne_range_damage']
		ctx["boss_ground_melee_damage"] = resultCalcDamg['boss_ground_melee_damage']
		ctx["boss_ground_range_damage"] = resultCalcDamg['boss_ground_range_damage']
		ctx["boss_airborne_melee_damage"] = resultCalcDamg['boss_airborne_melee_damage']
		ctx["boss_airborne_range_damage"] = resultCalcDamg['boss_airborne_range_damage']
		ctx["vars_dict"] =  runes_table_stats.getRunesDmgCalc()
	elif request.method == "POST":
		damage_calc_form = DamageCalculatorForm(request.POST)
		if damage_calc_form.is_valid() and 'runes' in request.POST:
			listHeroStepAtk = calc_user_dmg.hero_atk
			param_runes_display = runes_table_stats.getRunesDmgCalc()
			runes = damage_calc_form.cleaned_data['runes']
			first_select = request.POST.get('firstSelect',None)
			second_select = request.POST.get('secondSelect',None)
			third_select = request.POST.get('thirdSelect',None)
			fourth_select = request.POST.get('fourthSelect',None)
			fifth_select = request.POST.get('fifthSelect',None)
			first_input = damage_calc_form.cleaned_data['firstInput']
			second_input = damage_calc_form.cleaned_data['secondInput']
			third_input = damage_calc_form.cleaned_data['thirdInput']
			fourth_input = damage_calc_form.cleaned_data['fourthInput']
			fifth_input = damage_calc_form.cleaned_data['fifthInput']
			inputRune = {"none":0,'attack_flat':0,'attack_var':0.0,"flat_dmg_airborne":0,"var_dmg_airborne":0.0,
				"flat_dmg_ground":0,"var_dmg_ground":0.0,"flat_dmg_melee":0.0,"var_dmg_melee":0.0,
				"flat_dmg_ranged":0,"var_dmg_ranged":0.0,"flat_dmg_boss":0,"var_dmg_boss":0.0,"flat_dmg_mob":0,
				"var_dmg_mob":0.0,"var_dmg_hero":0.0,"flat_all_dmg":0.0,"var_all_dmg":0.0,"var_elemental_dmg":0.0,
				"var_atk_speed":0.0,"var_crit_rate":0.0,"var_crit_dmg":0.0,'Attack (Courage)':0,'Attack% (Courage)':0.0,
				'Hero base ATK':0,'Hero base ATK %':0.0,first_select: first_input,second_select: second_input,
				third_select: third_input,fourth_select: fourth_input,fifth_select: fifth_input}

			power_vars = {
				'atk_power_flat': inputRune['attack_flat'],
				'atk_power_var': inputRune['attack_var'],
				'atk_courage_flat': param_runes_display["atk_courage_flat"],
				'atk_courage_var': param_runes_display["atk_courage_var"],
				'courage_hero_atk_flat': param_runes_display["courage_hero_atk_flat"],
				'courage_hero_atk_var': param_runes_display["courage_hero_atk_var"],
				"power_second_select":second_select,
				"power_second_input":second_input,
				"power_third_select":third_select,
				"power_third_input":third_input,
				"power_fourth_select":fourth_select,
				"power_fourth_input":fourth_input,
				"power_fifth_select":fifth_select,
				"power_fifth_input":fifth_input
			}
			courage_vars = {
				'atk_power_flat': param_runes_display["atk_power_flat"],
				'atk_power_var': param_runes_display["atk_power_var"],
				'atk_courage_flat': inputRune['Attack (Courage)'],
				'atk_courage_var': inputRune['Attack% (Courage)'],
				'courage_hero_atk_flat': inputRune['Hero base ATK'],
				'courage_hero_atk_var': inputRune['Hero base ATK %'],
				"power_second_select":param_runes_display["power_second_select"],
				"power_second_input":param_runes_display["power_second_input"],
				"power_third_select":param_runes_display["power_third_select"],
				"power_third_input":param_runes_display["power_third_input"],
				"power_fourth_select":param_runes_display["power_fourth_select"],
				"power_fourth_input":param_runes_display["power_fourth_input"],
				"power_fifth_select":param_runes_display["power_fifth_select"],
				"power_fifth_input":param_runes_display["power_fifth_input"]
			}
			vars_dict = power_vars if runes == 'power' else courage_vars

			cumul_var_atk = (float(vars_dict['atk_power_var'])/100 + float(vars_dict['atk_courage_var'])/100 + float(listHeroStepAtk[2]))
			hero_modified_base_atk = (int(listHeroStepAtk[3]) - int(vars_dict['courage_hero_atk_flat'])) * (float(vars_dict['courage_hero_atk_var']) + float(listHeroStepAtk[4]) + 1) + int(vars_dict['courage_hero_atk_flat'])
			cumul_flat_atk = int(listHeroStepAtk[1]) + int(vars_dict['atk_power_flat']) + int(vars_dict['atk_courage_flat'])
			global_stats_atk_flat = round(int(hero_modified_base_atk) + int(cumul_flat_atk) + int(listHeroStepAtk[5]))
			global_stats_atk = global_stats_atk_flat + (global_stats_atk_flat*float(cumul_var_atk)) + (global_stats_atk_flat*float(listHeroStepAtk[6])) + (global_stats_atk_flat*float(listHeroStepAtk[7])) + listHeroStepAtk[8] + listHeroStepAtk[9]

			resultCalcDamg = calc_user_dmg.calculDamage(
				global_atk_save=global_stats_atk,
				crit_dmg=float(inputRune['var_crit_dmg'])+calc_user_dmg.crit_dmg,
				crit_rate=float(inputRune['var_crit_rate'])+calc_user_dmg.crit_rate,
				flat_dmg_vs_mobs=float(inputRune['flat_dmg_mob'])+calc_user_dmg.flat_dmg_vs_mobs,
				var_dmg_vs_mobs=float(inputRune['var_dmg_mob'])+calc_user_dmg.var_dmg_vs_mobs,
				flat_dmg_vs_ground=float(inputRune['flat_dmg_ground'])+calc_user_dmg.flat_dmg_vs_ground,
				var_dmg_vs_ground=float(inputRune['var_dmg_ground'])+calc_user_dmg.var_dmg_vs_ground,
				flat_dmg_vs_melee=float(inputRune['flat_dmg_melee'])+calc_user_dmg.flat_dmg_vs_melee,
				var_dmg_vs_melee=float(inputRune['var_dmg_melee'])+calc_user_dmg.var_dmg_vs_melee,
				flat_dmg_vs_airborne=float(inputRune['flat_dmg_airborne'])+calc_user_dmg.flat_dmg_vs_airborne,
				var_dmg_vs_airborne=float(inputRune['var_dmg_airborne'])+calc_user_dmg.var_dmg_vs_airborne,
				flat_dmg_vs_boss=float(inputRune['flat_dmg_boss'])+calc_user_dmg.flat_dmg_vs_boss,
				var_dmg_vs_boss=float(inputRune['var_dmg_boss'])+calc_user_dmg.var_dmg_vs_boss,
				flat_dmg_vs_range=float(inputRune['flat_dmg_ranged'])+calc_user_dmg.flat_dmg_vs_range,
				var_dmg_vs_range=float(inputRune['var_dmg_ranged'])+calc_user_dmg.var_dmg_vs_range,
				flat_dmg_all=float(inputRune['flat_all_dmg'])+calc_user_dmg.flat_dmg_all,
				var_dmg_all=float(inputRune['var_all_dmg'])+calc_user_dmg.var_dmg_all
			)
			ctx.update({
				"method": request.method,"runes": runes,"vars_dict":vars_dict,
				"firstSelect": first_select,"firstInput": first_input,"secondSelect": second_select,"secondInput": second_input,
				"thirdSelect": third_select,"thirdInput": third_input,"fourthSelect": fourth_select,"fourthInput": fourth_input,
				"fifthSelect": fifth_select,"fifthInput": fifth_input,"averageDamage": resultCalcDamg['averageDamageAll'],"crit_dmg": resultCalcDamg['crit_dmg'],
				"crit_rate": resultCalcDamg['crit_rate'],"mob_ground_melee_damage": resultCalcDamg['mob_ground_melee_damage'],"mob_ground_range_damage": resultCalcDamg['mob_ground_range_damage'],
				"mob_airborne_melee_damage": resultCalcDamg['mob_airborne_melee_damage'],"mob_airborne_range_damage": resultCalcDamg['mob_airborne_range_damage'],
				"boss_ground_melee_damage": resultCalcDamg['boss_ground_melee_damage'],"boss_ground_range_damage": resultCalcDamg['boss_ground_range_damage'],
				"boss_airborne_melee_damage": resultCalcDamg['boss_airborne_melee_damage'],"boss_airborne_range_damage": resultCalcDamg['boss_airborne_range_damage'],
			})
		else:
			form_error = damage_calc_form.errors.items()
			for k,v in form_error:
				error_msg = f"{k} : {str(v[0])}"
			messages.error(request, error_msg)
			return HttpResponseRedirect(f"/wiki/damage-calculator/{pbid}/")
	else:
		return HttpResponseRedirect(f"/wiki/damage-calculator/{pbid}/")
	ctx['damage_calc_form'] = damage_calc_form
	return render(request, "wiki/dmg_calc.html", ctx)


def handler404(request, exception):
	cookie_result = checkCookie(request.COOKIES)
	darkmode = checkTheme_Request(request,cookie_result)
	ctx = {
		'darkmode':darkmode,
		"header_msg":"Page Not Found",
		"lang":lang,
		"sidebarContent":SidebarContent
	}
	return render(request,'base/404.html', ctx, status=404)

def handler500(request):
	cookie_result = checkCookie(request.COOKIES)
	darkmode = checkTheme_Request(request,cookie_result)
	allfile = os.listdir('calculator/static/traceback_file/')
	for file in allfile:
		os.remove(f'calculator/static/traceback_file/{file}')
	exc_info = list(sys.exc_info())
	exc_output = list(traceback.format_exception(exc_info[1]))
	cookieRequest = checkCookie(request.COOKIES)
	try:
		username = list(cookieRequest)[0]
	except:
		username = 'unknown'
	with open(f'calculator/static/traceback_file/{username}.txt','a', encoding='utf-8') as exc_value:
		for i in exc_output:
			exc_value.write(i)
	webhook = DiscordWebhook(url=WEBHOOK_URL, content="<@&1091459966319198258>", rate_limit_retry=True, allowed_mentions={"users": ["382930544385851392"]})
	embed = DiscordEmbed(title='Error 500 - Internal Server Error', description='', color='963e3e')
	embed.set_author(
		name=username.capitalize(),
		icon_url="https://stats.wiki-archero.com/static/image/favicon.png",
	)
	embed.add_embed_field(name='Request', value=f"{request.method} | {request.path}", inline=False)
	embed.add_embed_field(name='Cookie', value=f"{request.COOKIES}", inline=False)
	webhook.add_embed(embed)
	with open(f'calculator/static/traceback_file/{username}.txt','r', encoding='utf-8') as f:
		webhook.add_file(file=f.read(), filename=f'{username}.txt')
	webhook.execute()
	return render(request,'base/500.html', {'darkmode':darkmode,"header_msg":"Internal Error Server", 'lang':lang,"sidebarContent":SidebarContent},status=500)


def rickroll(request):
	send_webhook(f'Someone has been rickrolled')	
	return HttpResponseRedirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


def tos(request):
	cookie_result = checkCookie(request.COOKIES)
	darkmode = checkTheme_Request(request,cookie_result)
	return render(request,'tos.html',{"darkmode": darkmode})

def changelog(request):
	cookie_result = checkCookie(request.COOKIES)
	darkmode = checkTheme_Request(request,cookie_result)
	with open(f'calculator/static/json/commits.json','r', encoding='utf-8') as commit:
		commit_json = json.load(commit)
	return render(request,'changelog.html',{"commit_json":commit_json,"darkmode": darkmode, "header_msg": "Change Log", 'lang':lang, "sidebarContent":SidebarContent})