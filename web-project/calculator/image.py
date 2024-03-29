from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

def round_jewel(jewel:int):
    if jewel >= 48:
        jewel = 48
    elif jewel >= 38:
        jewel = 38
    elif jewel >= 28:
        jewel = 28
    elif jewel >= 16:
        jewel = 16
    elif jewel >= 8:
        jewel = 8
    elif jewel >= 4:
        jewel = 4
    else:
        jewel=0
    return jewel

items={
    "demon_blade_rain":{
        "common":Path("calculator/static/image/items/demon_blade_rain_common.png"),
        "epic":Path("calculator/static/image/items/demon_blade_rain_epic.png"),
        "mythic":Path("calculator/static/image/items/demon_blade_rain_mythic.png"),
        "demon_blade_rain_1":Path("calculator/static/image/weapon_skin/demon_blade_rain_1.png"),
        "demon_blade_rain_2":Path("calculator/static/image/weapon_skin/demon_blade_rain_2.png")
    },
    "brave_bow":{
        "common":Path("calculator/static/image/items/brave_bow_common.png"),
        "epic":Path("calculator/static/image/items/brave_bow_epic.png"),
        "mythic":Path("calculator/static/image/items/brave_bow_mythic.png"),
        "brave_bow_1":Path("calculator/static/image/weapon_skin/brave_bow_1.png"),
        "brave_bow_2":Path("calculator/static/image/weapon_skin/brave_bow_2.png")
    },
    "brightspear":{
        "common":Path("calculator/static/image/items/brightspear_common.png"),
        "epic":Path("calculator/static/image/items/brightspear_epic.png"),
        "mythic":Path("calculator/static/image/items/brightspear_mythic.png"),
        "brightspear_1":Path("calculator/static/image/weapon_skin/brightspear_1.png"),
        "brightspear_2":Path("calculator/static/image/weapon_skin/brightspear_2.png")
    },
    "death_scythe":{
        "common":Path("calculator/static/image/items/death_scythe_common.png"),
        "epic":Path("calculator/static/image/items/death_scythe_epic.png"),
        "mythic":Path("calculator/static/image/items/death_scythe_mythic.png"),
        "death_scythe_1":Path("calculator/static/image/weapon_skin/death_scythe_1.png"),
        "death_scythe_2":Path("calculator/static/image/weapon_skin/death_scythe_2.png")
    },
    "gale_force":{
        "common":Path("calculator/static/image/items/gale_force_common.png"),
        "epic":Path("calculator/static/image/items/gale_force_epic.png"),
        "mythic":Path("calculator/static/image/items/gale_force_mythic.png"),
        "gale_force_1":Path("calculator/static/image/weapon_skin/gale_force_1.png"),
        "gale_force_2":Path("calculator/static/image/weapon_skin/gale_force_2.png")
    },
    "mini_atreus":{
        "common":Path("calculator/static/image/items/mini_atreus.png"),
        "epic":Path("calculator/static/image/items/mini_atreus.png"),
        "mythic":Path("calculator/static/image/items/mini_atreus.png")
    },
    "saw_blade":{
        "common":Path("calculator/static/image/items/saw_blade_common.png"),
        "epic":Path("calculator/static/image/items/saw_blade_epic.png"),
        "mythic":Path("calculator/static/image/items/saw_blade_mythic.png"),
        "saw_blade_1":Path("calculator/static/image/weapon_skin/saw_blade_1.png"),
        "saw_blade_2":Path("calculator/static/image/weapon_skin/saw_blade_2.png")
    },
    "stalker_staff":{
        "common":Path("calculator/static/image/items/stalker_staff_common.png"),
        "epic":Path("calculator/static/image/items/stalker_staff_epic.png"),
        "mythic":Path("calculator/static/image/items/stalker_staff_mythic.png"),
        "stalker_staff_1":Path("calculator/static/image/weapon_skin/stalker_staff_1.png"),
        "stalker_staff_2":Path("calculator/static/image/weapon_skin/stalker_staff_2.png")
    },
    "tornado":{
        "common":Path("calculator/static/image/items/tornado_common.png"),
        "epic":Path("calculator/static/image/items/tornado_epic.png"),
        "mythic":Path("calculator/static/image/items/tornado_mythic.png"),
        "boomerang_1":Path("calculator/static/image/weapon_skin/boomerang_1.png"),
        "boomerang_2":Path("calculator/static/image/weapon_skin/boomerang_2.png")
    },
    "antiquated_sword":{
        "common":Path("calculator/static/image/items/antiquated_sword_common.png"),
        "epic":Path("calculator/static/image/items/antiquated_sword_epic.png"),
        "mythic":Path("calculator/static/image/items/antiquated_sword_mythic.png"),
        "antiquated_sword_1":Path("calculator/static/image/weapon_skin/antiquated_sword_1.png"),
        "antiquated_sword_2":Path("calculator/static/image/weapon_skin/antiquated_sword_2.png")
    },
    "expedition_fist":{
        "common":Path("calculator/static/image/items/expedition_fist_epic.png"),
        "epic":Path("calculator/static/image/items/expedition_fist_epic.png"),
        "mythic":Path("calculator/static/image/items/expedition_fist_mythic.png"),
    },

    "bright_robe":Path("calculator/static/image/items/bright_robe.png"),
    "golden_chestplate":Path("calculator/static/image/items/golden_chestplate.png"),
    "phantom_cloak":Path("calculator/static/image/items/phantom_cloak.png"),
    "shadow_robe":Path("calculator/static/image/items/shadow_robe.png"),
    "vest_of_dexterity":Path("calculator/static/image/items/vest_of_dexterity.png"),
    "void_robe":Path("calculator/static/image/items/void_robe.png"),
    "expedition_plate":Path("calculator/static/image/items/expedition_plate.png"),

    "vilebat_ring":{
        "common":Path("calculator/static/image/items/vilebat_ring_common.png"),
        "epic":Path("calculator/static/image/items/vilebat_ring_epic.png")
    },
    "dragon_ring":{
        "common":Path("calculator/static/image/items/dragon_ring_common.png"),
        "epic":Path("calculator/static/image/items/dragon_ring_epic.png")
    },
    "bear_ring":{
        "common":Path("calculator/static/image/items/bear_ring_common.png"),
        "epic":Path("calculator/static/image/items/bear_ring_epic.png")
    },
    "bull_ring":{
        "common":Path("calculator/static/image/items/bull_ring_common.png"),
        "epic":Path("calculator/static/image/items/bull_ring_epic.png")
    },
    "falcon_ring":{
        "common":Path("calculator/static/image/items/falcon_ring_common.png"),
        "epic":Path("calculator/static/image/items/falcon_ring_epic.png")
    },
    "lion_ring":{
        "common":Path("calculator/static/image/items/lion_ring_common.png"),
        "epic":Path("calculator/static/image/items/lion_ring_epic.png")
    },
    "serpent_ring":{
        "common":Path("calculator/static/image/items/serpent_ring_common.png"),
        "epic":Path("calculator/static/image/items/serpent_ring_epic.png")
    },
    "wolf_ring":{
        "common":Path("calculator/static/image/items/wolf_ring_common.png"),
        "epic":Path("calculator/static/image/items/wolf_ring_epic.png")
    },
    "expedition_ring":{
        "common":Path("calculator/static/image/items/expedition_ring.png"),
        "epic":Path("calculator/static/image/items/expedition_ring.png")
    },

    "bone_warrior":Path("calculator/static/image/items/bone_warrior.png"),
    "elf":Path("calculator/static/image/items/elf.png"),
    "flaming_ghost":Path("calculator/static/image/items/flaming_ghost.png"),
    "laser_bat":Path("calculator/static/image/items/laser_bat.png"),
    "living_bomb":Path("calculator/static/image/items/living_bomb.png"),
    "noisy_owl":Path("calculator/static/image/items/noisy_owl.png"),
    "scythe_mage":Path("calculator/static/image/items/scythe_mage.png"),

    "blazing_bracelet":Path("calculator/static/image/items/blazing_bracelet.png"),
    "frozen_bracelet":Path("calculator/static/image/items/frozen_bracelet.png"),
    "invincible_bracelet":Path("calculator/static/image/items/invincible_bracelet.png"),
    "quickshot_bracelet":Path("calculator/static/image/items/quickshot_bracelet.png"),
    "split_bracelet":Path("calculator/static/image/items/split_bracelet.png"),
    "thunder_bracelet":Path("calculator/static/image/items/thunder_bracelet.png"),
    "shield_bracelet":Path("calculator/static/image/items/shield_bracelet.png"),
    "expedition_bracelet":Path("calculator/static/image/items/expedition_bracelet.png"),

    "agile_locket":Path("calculator/static/image/items/agile_locket.png"),
    "angel_locket":Path("calculator/static/image/items/angel_locket.png"),
    "bloodthirsty_locket":Path("calculator/static/image/items/bloodthirsty_locket.png"),
    "bulletproof_locket":Path("calculator/static/image/items/bulletproof_locket.png"),
    "iron_locket":Path("calculator/static/image/items/iron_locket.png"),
    "piercer_locket":Path("calculator/static/image/items/piercer_locket.png"),
    "counterattack_locket":Path("calculator/static/image/items/counterattack_locket.png"),
    "expedition_locket":Path("calculator/static/image/items/expedition_locket.png"),

    "arcane_archer":Path("calculator/static/image/items/arcane_archer.png"),
    "art_of_combat":Path("calculator/static/image/items/art_of_combat.png"),
    "enlightenment":Path("calculator/static/image/items/enlightenment.png"),
    "giants_contract":Path("calculator/static/image/items/giants_contract.png"),
    "ice_realm":Path("calculator/static/image/items/ice_realm.png"),
    "spectre_book":Path("calculator/static/image/items/spectre_book.png"),
    "arcanum_of_time":Path("calculator/static/image/items/arcanum_of_time.png"),
    "expedition_spellbook":Path("calculator/static/image/items/expedition_spellbook.png"),

    "none":Path("calculator/static/image/items/none.png"),
    "none_dict":{
        "common":Path("calculator/static/image/items/none.png")
    }
}

list_s_eqpm = {
    "weapon": ["expedition_fist"],
    "armor": ["expedition_plate"],
    "ring": ["expedition_ring"],
    "bracelet": ["expedition_bracelet"],
    "locket": ["expedition_locket"],
    "spellbook": ["expedition_spellbook"]
}

rarity_weapon={
    "none":"common",
    "common":"common",
    "great":"common",
    "rare":"common",
    "epic":"epic",
    "perfect_epic":"epic",
    "legendary":"epic",
    "ancient_legendary":"epic",
    "mythic":"mythic",
    "mythic_1":"mythic",
    "mythic_2":"mythic",
    "titan_tales":"mythic",
    "titan_tales_1":"mythic",
    "titan_tales_2":"mythic",
    "titan_tales_3":"mythic",
    "chaos":"mythic",
}

rarity_ring={
    "none":"common",
    "common":"common",
    "great":"common",
    "rare":"common",
    "epic":"epic",
    "perfect_epic":"epic",
    "legendary":"epic",
    "ancient_legendary":"epic",
    "mythic":"epic",
    "mythic_1":"epic",
    "mythic_2":"epic",
    "titan_tales":"epic",
    "titan_tales_1":"epic",
    "titan_tales_2":"epic",
    "titan_tales_3":"epic",
    "chaos":"epic",
}

fond_items={
    "common":Path("calculator/static/image/rarity/common.png"),
    "great":Path("calculator/static/image/rarity/great.png"),
    "rare":Path("calculator/static/image/rarity/rare.png"),
    "epic":Path("calculator/static/image/rarity/epic.png"),
    "perfect_epic":Path("calculator/static/image/rarity/perfect_epic.png"),
    "legendary":Path("calculator/static/image/rarity/legendary.png"),
    "ancient_legendary":Path("calculator/static/image/rarity/ancient_legendary.png"),
    "mythic":Path("calculator/static/image/rarity/mythic.png"),
    "mythic_1":Path("calculator/static/image/rarity/mythic.png"),
    "mythic_2":Path("calculator/static/image/rarity/mythic.png"),
    "titan_tales":Path("calculator/static/image/rarity/titan_tales.png"),
    "titan_tales_1":Path("calculator/static/image/rarity/titan_tales.png"),
    "titan_tales_2":Path("calculator/static/image/rarity/titan_tales.png"),
    "titan_tales_3":Path("calculator/static/image/rarity/titan_tales.png"),
    "chaos":Path("calculator/static/image/rarity/chaos.png"),

    "none":Path("calculator/static/image/items/none.png")
}

subQuality = {
    "mythic_1":Path("calculator/static/image/rarity/SubQuality_8.png"),
    "mythic_2":Path("calculator/static/image/rarity/SubQuality_8.png"),
    "titan_tales_1":Path("calculator/static/image/rarity/SubQuality_9.png"),
    "titan_tales_2":Path("calculator/static/image/rarity/SubQuality_9.png"),
    "titan_tales_3":Path("calculator/static/image/rarity/SubQuality_9.png"),
}

heros={
    "Atreus":{
        "vest_of_dexterity":Path("calculator/static/image/heros/Atreus_vest_of_dexterity.png"),
        "void_robe":Path("calculator/static/image/heros/Atreus_void_robe.png"),
        "shadow_robe":Path("calculator/static/image/heros/Atreus_shadow_robe.png"),
        "phantom_cloak":Path("calculator/static/image/heros/Atreus_phantom_cloak.png"),
        "golden_chestplate":Path("calculator/static/image/heros/Atreus_golden_chestplate.png"),
        "bright_robe":Path("calculator/static/image/heros/Atreus_bright_robe.png"),
        "expedition_plate":Path("calculator/static/image/heros/Atreus_none.png"), # TODO add Atreus cropped photo with expedition plate
        "none":Path("calculator/static/image/heros/Atreus_none.png"),
    },
    "Phoren":Path("calculator/static/image/heros/Phoren.png"),
    "Urasil":Path("calculator/static/image/heros/Urasil.png"),
    "Helix":Path("calculator/static/image/heros/Helix.png"),
    "Meowgik":Path("calculator/static/image/heros/Meowgik.png"),
    "Shari":Path("calculator/static/image/heros/Shari.png"),
    "Ayana":Path("calculator/static/image/heros/Ayana.png"),
    "Onir":Path("calculator/static/image/heros/Onir.png"),
    "Rolla":Path("calculator/static/image/heros/Rolla.png"),
    "Bonnie":Path("calculator/static/image/heros/Bonnie.png"),
    "Ophelia":Path("calculator/static/image/heros/Ophelia.png"),
    "Taranis":Path("calculator/static/image/heros/Taranis.png"),
    "Sylvan":Path("calculator/static/image/heros/Sylvan.png"),
    "Shade":Path("calculator/static/image/heros/Shade.png"),
    "Ryan":Path("calculator/static/image/heros/Ryan.png"),
    "Lina":Path("calculator/static/image/heros/Lina.png"),
    "Aquea":Path("calculator/static/image/heros/Aquea.png"),
    "Shingen":Path("calculator/static/image/heros/Shingen.png"),
    "Gugu":Path("calculator/static/image/heros/Gugu.png"),
    "Iris":Path("calculator/static/image/heros/Iris.png"),
    "Blazo":Path("calculator/static/image/heros/Blazo.png"),
    "Melinda":Path("calculator/static/image/heros/Melinda.png"),
    "Elaine":Path("calculator/static/image/heros/Elaine.png"),
    "Bobo":Path("calculator/static/image/heros/Bobo.png"),
    "Stella":Path("calculator/static/image/heros/Stella2.png"),
    "Taiga":Path("calculator/static/image/heros/Taiga.png"),
}

jewel = {
    -1:Path("calculator/static/image/round_jewel/base.png"), #pour le fond
    0:Path("calculator/static/image/round_jewel/None.png"),
    4:Path("calculator/static/image/round_jewel/gris.png"),
    8:Path("calculator/static/image/round_jewel/vert.png"),
    16:Path("calculator/static/image/round_jewel/bleu.png"),
    28:Path("calculator/static/image/round_jewel/rose.png"),
    38:Path("calculator/static/image/round_jewel/or.png"),
    48:Path("calculator/static/image/round_jewel/red.png")
}

position = {
    "weapon": (78,80), ## (from the left, from the bottom)
    "armor": (930,80),
    "ring1": (78,330),
    "ring2": (930,330),
    "pet1": (78,580),
    "pet2": (930,580),
    "bracelet": (78,832),
    "book": (494,822),
    "locket": (930,832),

    "s_icon_weapon": (55,220), ## (from the left, from the bottom)
    "s_icon_armor": (905,220),
    "s_icon_ring1": (55,470),
    "s_icon_ring2": (905,470),
    "s_icon_bracelet": (55,970),
    "s_icon_locket": (905,970),
    "s_icon_spellbook": (470,978),

    "jewel_weapon": (56,68), ## (from the left, from the bottom)
    "jewel_armor": (907,68),
    "jewel_ring1": (56,320),
    "jewel_ring2": (907,320),
    "jewel_pet1": (56,574),
    "jewel_pet2": (907,574),
    "jewel_bracelet": (56,822),
    "jewel_book": (476,812),
    "jewel_locket": (907,822),

    "bg_jewel_weapon": (54,64), ## (from the left, from the bottom)
    "bg_jewel_armor": (905,64),
    "bg_jewel_ring1": (54,316),
    "bg_jewel_ring2": (905,316),
    "bg_jewel_pet1": (54,570),
    "bg_jewel_pet2": (905,570),
    "bg_jewel_bracelet": (54,818),
    "bg_jewel_book": (476,812),
    "bg_jewel_locket": (905,818),

    "hero": (375,64),
    "hero_elaine": (240,145),
    "hero_stella": (220,66),

    "lvl_weapon": (185,268), ## (from the left, from the bottom)
    "lvl_armor": (1045,268),
    "lvl_ring1": (185,520),
    "lvl_ring2": (1045,520),
    "lvl_pet1": (185,768),
    "lvl_pet2": (1045,768),
    "lvl_bracelet": (185,1020),
    "lvl_book": (620,1030),
    "lvl_locket": (1045,1020),

    "button_jewel": (1017,1097),

    "dragon": (320,-5),
    "dragon_rank": (335,135),
    "dragon_image": (810,1064),

    "subQuality_weapon": (154, 62), ## (from the left, from the bottom)
    "subQuality_armor": (1008, 62),
    "subQuality_ring1": (154, 312),
    "subQuality_ring2": (1008, 312),
    "subQuality_pet1": (154, 558),
    "subQuality_pet2": (1008, 558),
    "subQuality_locket": (1008, 812),
    "subQuality_bracelet": (154, 812),
    "subQuality_book": (580, 806),
}

font_lvl = ImageFont.truetype("calculator/static/fonts/magic.otf",35)

letter_dragon={
    "None":"A",
    "Stormra":"A",
    "Infernox":"A",
    "Noxion":"A",
    "Glacion":"A",
    "Dominus":"A",
    "Jadeon":"A",
    "Shadex":"A",
    "Ferron":"S",
    "Geogon":"S",
    "Swordian":"S",
    "Necrogon":"S",
    "Starrite":"SS",
    "Voideon":"SS",
    "Magmar":"SS"
}

dragon = {
    "None":Path("calculator/static/image/dragon/none.png"),
    "Stormra":Path("calculator/static/image/dragon/Stormra.png"),
    "Infernox":Path("calculator/static/image/dragon/Infernox.png"),
    "Noxion":Path("calculator/static/image/dragon/Noxion.png"),
    "Glacion":Path("calculator/static/image/dragon/Glacion.png"),
    "Dominus":Path("calculator/static/image/dragon/Dominus.png"), 
    "Jadeon":Path("calculator/static/image/dragon/Jadeon.png"), 
    "Shadex":Path("calculator/static/image/dragon/Shadex.png"),
    "Ferron":Path("calculator/static/image/dragon/Ferron.png"),
    "Geogon":Path("calculator/static/image/dragon/Geogon.png"),
    "Swordian":Path("calculator/static/image/dragon/Swordian.png"),
    "Necrogon":Path("calculator/static/image/dragon/Necrogon.png"),
    "Starrite":Path("calculator/static/image/dragon/Starrite.png"),
    "Voideon":Path("calculator/static/image/dragon/Voideon.png"), 
    "Magmar":Path("calculator/static/image/dragon/Magmar.png"), 
    "none":Path("calculator/static/image/dragon/none.png"),
    "Great":Path("calculator/static/image/dragon/great.png"),
    "Rare":Path("calculator/static/image/dragon/rare.png"),
    "Epic":Path("calculator/static/image/dragon/epic.png"),
    "Perfect_Epic":Path("calculator/static/image/dragon/epic.png"),
    "Legendary":Path("calculator/static/image/dragon/legendary.png"),
    "Ancient_Legendary":Path("calculator/static/image/dragon/legendary.png"),
    "Mythic":Path("calculator/static/image/dragon/mythic.png"),
    "A":Path("calculator/static/image/dragon/A.png"),
    "S":Path("calculator/static/image/dragon/S.png"),
    "SS":Path("calculator/static/image/dragon/SS.png")
}

s_grade_eqpm = Path("calculator/static/image/dragon/S.png")
button_jewel = Path("calculator/static/image/round_jewel/button.png")


def create_image(pbid:str,weapon_name:str,weapon_rarity:str,weapon_lvl:int,
    armor_name:str,armor_rarity:str,armor_lvl:int,ring_name1:str,ring_rarity1:str,ring_lvl1:int,
    ring_name2:str,ring_rarity2:str,ring_lvl2:int,pet_name1:str,pet_rarity1:str,pet_lvl1:int,
    pet_name2:str,pet_rarity2:str,pet_lvl2:int,bracelet_name:str,bracelet_rarity:str,bracelet_lvl:int,
    locket_name:str,locket_rarity:str,locket_lvl:int,book_name:str,book_rarity:str,book_lvl:int,
    atk:int,pv:int,jewel_weapon:int,jewel_armor:int,jewel_ring1:int,jewel_ring2:int,jewel_pet1:int,
    jewel_pet2:int,jewel_bracelet:int,jewel_locket:int,jewel_book:int,hero:str,dragon_name1:str,dragon_name2:str,
    dragon_name3:str,dragon_rarity1:str,dragon_rarity2:str,dragon_rarity3:str, weapon_skin_activ:str):

    if weapon_name == "none":
        weapon_name = "none_dict"
        weapon_rarity = "none"
        weapon_lvl = ""
    else:
        weapon_lvl = f"{weapon_lvl}"
    if armor_name == "none":
        armor_rarity = "none"
        armor_lvl = ""
    else:
        armor_lvl = f"{armor_lvl}"
    if ring_name1 == "none":
        ring_name1 = "none_dict"
        ring_rarity1 = "none"
        ring_lvl1 = ""
    else:
        ring_lvl1 = f"{ring_lvl1}"
    if ring_name2 == "none":
        ring_name2 = "none_dict"
        ring_rarity2 = "none"
        ring_lvl2 = ""
    else:
        ring_lvl2 = f"{ring_lvl2}"
    if pet_name1 == "none":
        pet_rarity1 = "none"
        pet_lvl1 = ""
    else:
        pet_lvl1 = f"{pet_lvl1}"
    if pet_name2 == "none":
        pet_rarity2 = "none"
        pet_lvl2 = ""
    else:
        pet_lvl2 = f"{pet_lvl2}"
    if bracelet_name == "none":
        bracelet_rarity = "none"
        bracelet_lvl = ""
    else:
        bracelet_lvl = f"{bracelet_lvl}"
    if book_name == "none":
        book_rarity = "none"
        book_lvl = ""
    else:
        book_lvl = f"{book_lvl}"
    if locket_name == "none":
        locket_rarity = "none"
        locket_lvl = ""
    else:
        locket_lvl = f"{locket_lvl}"

    base = Image.open(Path("calculator/static/image/background/bg_stuff_affiche.png"))

    base.paste(im=Image.open(fond_items[weapon_rarity]).resize((218,218)),
        box=position["weapon"],mask=Image.open(fond_items[weapon_rarity]).resize((218,218)))
    base.paste(im=Image.open(fond_items[armor_rarity]).resize((218,218)),
        box=position["armor"],mask=Image.open(fond_items[armor_rarity]).resize((218,218)))
    base.paste(im=Image.open(fond_items[ring_rarity1]).resize((218,218)),
        box=position["ring1"],mask=Image.open(fond_items[ring_rarity1]).resize((218,218)))
    base.paste(im=Image.open(fond_items[ring_rarity2]).resize((218,218)),
        box=position["ring2"],mask=Image.open(fond_items[ring_rarity2]).resize((218,218)))
    base.paste(im=Image.open(fond_items[pet_rarity1]).resize((218,218)),
        box=position["pet1"],mask=Image.open(fond_items[pet_rarity1]).resize((218,218)))
    base.paste(im=Image.open(fond_items[pet_rarity2]).resize((218,218)),
        box=position["pet2"],mask=Image.open(fond_items[pet_rarity2]).resize((218,218)))
    base.paste(im=Image.open(fond_items[bracelet_rarity]).resize((218,218)),
        box=position["bracelet"],mask=Image.open(fond_items[bracelet_rarity]).resize((218,218)))
    base.paste(im=Image.open(fond_items[book_rarity]).resize((235,235)),
        box=position["book"],mask=Image.open(fond_items[book_rarity]).resize((235,235)))
    base.paste(im=Image.open(fond_items[locket_rarity]).resize((218,218)),
        box=position["locket"],mask=Image.open(fond_items[locket_rarity]).resize((218,218)))

    if weapon_skin_activ == "None":
        base.paste(im=Image.open(items[weapon_name].get(rarity_weapon[weapon_rarity],"common")).resize((218,218)),
            box=position["weapon"],mask=Image.open(items[weapon_name][rarity_weapon[weapon_rarity]]).resize((218,218)))
    else:
        base.paste(im=Image.open(items[weapon_name][weapon_skin_activ]).resize((218,218)),
            box=position["weapon"],mask=Image.open(items[weapon_name][weapon_skin_activ]).resize((218,218)))
    base.paste(im=Image.open(items[armor_name]).resize((218,218)),
        box=position["armor"],mask=Image.open(items[armor_name]).resize((218,218)))
    base.paste(im=Image.open(items[ring_name1][rarity_ring[ring_rarity1]]).resize((218,218)),
        box=position["ring1"],mask=Image.open(items[ring_name1][rarity_ring[ring_rarity1]]).resize((218,218)))
    base.paste(im=Image.open(items[ring_name2][rarity_ring[ring_rarity2]]).resize((218,218)),
        box=position["ring2"],mask=Image.open(items[ring_name2][rarity_ring[ring_rarity2]]).resize((218,218)))
    base.paste(im=Image.open(items[pet_name1]).resize((218,218)),
        box=position["pet1"],mask=Image.open(items[pet_name1]).resize((218,218)))
    base.paste(im=Image.open(items[pet_name2]).resize((218,218)),
        box=position["pet2"],mask=Image.open(items[pet_name2]).resize((218,218)))
    base.paste(im=Image.open(items[bracelet_name]).resize((218,218)),
        box=position["bracelet"],mask=Image.open(items[bracelet_name]).resize((218,218)))
    base.paste(im=Image.open(items[book_name]).resize((235,235)),
        box=position["book"],mask=Image.open(items[book_name]).resize((235,235)))
    base.paste(im=Image.open(items[locket_name]).resize((218,218)),
        box=position["locket"],mask=Image.open(items[locket_name]).resize((218,218)))

    if weapon_name in list_s_eqpm['weapon']: base.paste(im=Image.open(s_grade_eqpm).resize((82,82)),box=position["s_icon_weapon"],mask=Image.open(s_grade_eqpm).resize((82,82)))
    if armor_name in list_s_eqpm['armor']: base.paste(Image.open(s_grade_eqpm).resize((82,82)),box=position["s_icon_armor"],mask=Image.open(s_grade_eqpm).resize((82,82)))
    if ring_name1 in list_s_eqpm['ring']: base.paste(Image.open(s_grade_eqpm).resize((82,82)),box=position["s_icon_ring1"],mask=Image.open(s_grade_eqpm).resize((82,82)))
    if ring_name2 in list_s_eqpm['ring']: base.paste(Image.open(s_grade_eqpm).resize((82,82)),box=position["s_icon_ring2"],mask=Image.open(s_grade_eqpm).resize((82,82)))
    if bracelet_name in list_s_eqpm['bracelet']: base.paste(Image.open(s_grade_eqpm).resize((82,82)),box=position["s_icon_bracelet"],mask=Image.open(s_grade_eqpm).resize((82,82)))
    if locket_name in list_s_eqpm['locket']: base.paste(Image.open(s_grade_eqpm).resize((82,82)),box=position["s_icon_locket"],mask=Image.open(s_grade_eqpm).resize((82,82)))
    if book_name in list_s_eqpm['spellbook']: base.paste(Image.open(s_grade_eqpm).resize((82,82)),box=position["s_icon_spellbook"],mask=Image.open(s_grade_eqpm).resize((82,82)))

    number_SubQuality = ImageDraw.Draw(base)
    if weapon_rarity[-1].isdigit():
        number = weapon_rarity.split('_')[-1]
        base.paste(im=Image.open(subQuality[weapon_rarity]).resize((62,62)),box=position["subQuality_weapon"],mask=Image.open(subQuality[weapon_rarity]).resize((62,62)))
        number_SubQuality.text((175,72),str(number),(255,255,255),font=ImageFont.truetype("calculator/static/fonts/archero_font_white.otf",40))
        number_SubQuality.text((175,72),str(number),(0,0,0),font=ImageFont.truetype("calculator/static/fonts/archero_font_black.otf",40))
    if armor_rarity[-1].isdigit():
        number = armor_rarity.split('_')[-1]
        base.paste(im=Image.open(subQuality[armor_rarity]).resize((62,62)),box=position["subQuality_armor"],mask=Image.open(subQuality[armor_rarity]).resize((62,62)))
        number_SubQuality.text((1029,72),str(number),(255,255,255),font=ImageFont.truetype("calculator/static/fonts/archero_font_white.otf",40))
        number_SubQuality.text((1029,72),str(number),(0,0,0),font=ImageFont.truetype("calculator/static/fonts/archero_font_black.otf",40))
    if ring_rarity1[-1].isdigit():
        number = ring_rarity1.split('_')[-1]
        base.paste(im=Image.open(subQuality[ring_rarity1]).resize((62,62)),box=position["subQuality_ring1"],mask=Image.open(subQuality[ring_rarity1]).resize((62,62)))
        number_SubQuality.text((175,324),str(number),(255,255,255),font=ImageFont.truetype("calculator/static/fonts/archero_font_white.otf",40))
        number_SubQuality.text((175,324),str(number),(0,0,0),font=ImageFont.truetype("calculator/static/fonts/archero_font_black.otf",40))
    if ring_rarity2[-1].isdigit():
        number = ring_rarity2.split('_')[-1]
        base.paste(im=Image.open(subQuality[ring_rarity2]).resize((62,62)),box=position["subQuality_ring2"],mask=Image.open(subQuality[ring_rarity2]).resize((62,62)))
        number_SubQuality.text((1029,324),str(number),(255,255,255),font=ImageFont.truetype("calculator/static/fonts/archero_font_white.otf",40))
        number_SubQuality.text((1029,324),str(number),(0,0,0),font=ImageFont.truetype("calculator/static/fonts/archero_font_black.otf",40))
    if pet_rarity1[-1].isdigit():
        number = pet_rarity1.split('_')[-1]
        base.paste(im=Image.open(subQuality[pet_rarity1]).resize((62,62)),box=position["subQuality_pet1"],mask=Image.open(subQuality[pet_rarity1]).resize((62,62)))
        number_SubQuality.text((175,569),str(number),(255,255,255),font=ImageFont.truetype("calculator/static/fonts/archero_font_white.otf",40))
        number_SubQuality.text((175,569),str(number),(0,0,0),font=ImageFont.truetype("calculator/static/fonts/archero_font_black.otf",40))
    if pet_rarity2[-1].isdigit():
        number = pet_rarity2.split('_')[-1]
        base.paste(im=Image.open(subQuality[pet_rarity2]).resize((62,62)),box=position["subQuality_pet2"],mask=Image.open(subQuality[pet_rarity2]).resize((62,62)))
        number_SubQuality.text((1029,569),str(number),(255,255,255),font=ImageFont.truetype("calculator/static/fonts/archero_font_white.otf",40))
        number_SubQuality.text((1029,569),str(number),(0,0,0),font=ImageFont.truetype("calculator/static/fonts/archero_font_black.otf",40))
    if locket_rarity[-1].isdigit():
        number = locket_rarity.split('_')[-1]
        base.paste(im=Image.open(subQuality[locket_rarity]).resize((62,62)),box=position["subQuality_locket"],mask=Image.open(subQuality[locket_rarity]).resize((62,62)))
        number_SubQuality.text((1029,824),str(number),(255,255,255),font=ImageFont.truetype("calculator/static/fonts/archero_font_white.otf",40))
        number_SubQuality.text((1029,824),str(number),(0,0,0),font=ImageFont.truetype("calculator/static/fonts/archero_font_black.otf",40))
    if bracelet_rarity[-1].isdigit():
        number = bracelet_rarity.split('_')[-1]
        base.paste(im=Image.open(subQuality[bracelet_rarity]).resize((62,62)),box=position["subQuality_bracelet"],mask=Image.open(subQuality[bracelet_rarity]).resize((62,62)))
        number_SubQuality.text((175,824),str(number),(255,255,255),font=ImageFont.truetype("calculator/static/fonts/archero_font_white.otf",40))
        number_SubQuality.text((175,824),str(number),(0,0,0),font=ImageFont.truetype("calculator/static/fonts/archero_font_black.otf",40))
    if book_rarity[-1].isdigit():
        number = book_rarity.split('_')[-1]
        base.paste(im=Image.open(subQuality[book_rarity]).resize((62,62)),box=position["subQuality_book"],mask=Image.open(subQuality[book_rarity]).resize((62,62)))
        number_SubQuality.text((602,816),str(number),(255,255,255),font=ImageFont.truetype("calculator/static/fonts/archero_font_white.otf",40))
        number_SubQuality.text((602,816),str(number),(0,0,0),font=ImageFont.truetype("calculator/static/fonts/archero_font_black.otf",40))
    
    base.paste(Image.open(jewel[-1]).resize((82,82)),box=position["bg_jewel_weapon"],mask=Image.open(jewel[-1]).resize((82,82)))
    base.paste(Image.open(jewel[-1]).resize((82,82)),box=position["bg_jewel_armor"],mask=Image.open(jewel[-1]).resize((82,82)))
    base.paste(Image.open(jewel[-1]).resize((82,82)),box=position["bg_jewel_ring1"],mask=Image.open(jewel[-1]).resize((82,82)))
    base.paste(Image.open(jewel[-1]).resize((82,82)),box=position["bg_jewel_ring2"],mask=Image.open(jewel[-1]).resize((82,82)))
    base.paste(Image.open(jewel[-1]).resize((82,82)),box=position["bg_jewel_pet1"],mask=Image.open(jewel[-1]).resize((82,82)))
    base.paste(Image.open(jewel[-1]).resize((82,82)),box=position["bg_jewel_pet2"],mask=Image.open(jewel[-1]).resize((82,82)))
    base.paste(Image.open(jewel[-1]).resize((82,82)),box=position["bg_jewel_bracelet"],mask=Image.open(jewel[-1]).resize((82,82)))
    base.paste(Image.open(jewel[-1]).resize((82,82)),box=position["bg_jewel_locket"],mask=Image.open(jewel[-1]).resize((82,82)))

    base.paste(Image.open(jewel[round_jewel(jewel_weapon)]).resize((78,78)),box=position["jewel_weapon"],mask=Image.open(jewel[round_jewel(jewel_weapon)]).resize((78,78)))
    base.paste(Image.open(jewel[round_jewel(jewel_armor)]).resize((78,78)),box=position["jewel_armor"],mask=Image.open(jewel[round_jewel(jewel_armor)]).resize((78,78)))
    base.paste(Image.open(jewel[round_jewel(jewel_ring1)]).resize((78,78)),box=position["jewel_ring1"],mask=Image.open(jewel[round_jewel(jewel_ring1)]).resize((78,78)))
    base.paste(Image.open(jewel[round_jewel(jewel_ring2)]).resize((78,78)),box=position["jewel_ring2"],mask=Image.open(jewel[round_jewel(jewel_ring2)]).resize((78,78)))
    base.paste(Image.open(jewel[round_jewel(jewel_pet1)]).resize((78,78)),box=position["jewel_pet1"],mask=Image.open(jewel[round_jewel(jewel_pet1)]).resize((78,78)))
    base.paste(Image.open(jewel[round_jewel(jewel_pet2)]).resize((78,78)),box=position["jewel_pet2"],mask=Image.open(jewel[round_jewel(jewel_pet2)]).resize((78,78)))
    base.paste(Image.open(jewel[round_jewel(jewel_bracelet)]).resize((78,78)),box=position["jewel_bracelet"],mask=Image.open(jewel[round_jewel(jewel_bracelet)]).resize((78,78)))
    base.paste(Image.open(jewel[round_jewel(jewel_locket)]).resize((78,78)),box=position["jewel_locket"],mask=Image.open(jewel[round_jewel(jewel_locket)]).resize((78,78)))

    if hero == "Atreus":
        base.paste(im=Image.open(heros["Atreus"][armor_name]),box=position["hero"],mask=Image.open(heros["Atreus"][armor_name]))
    elif hero == "Elaine":
        base.paste(im=Image.open(heros[hero]),box=position["hero_elaine"],mask=Image.open(heros[hero]))
    elif hero == "Stella":
        base.paste(im=Image.open(heros[hero]),box=position["hero_stella"],mask=Image.open(heros[hero]))
    else:
        base.paste(im=Image.open(heros[hero]),box=position["hero"],mask=Image.open(heros[hero]))

    base.paste(Image.open(jewel[-1]).resize((82,82)),box=position["bg_jewel_book"],mask=Image.open(jewel[-1]).resize((82,82))) ## pour que il soit au dessus des pieds du héros
    base.paste(Image.open(jewel[round_jewel(jewel_book)]).resize((80,80)),box=position["jewel_book"],mask=Image.open(jewel[round_jewel(jewel_book)]).resize((80,80))) ## pour que il soit au dessus des pieds du héros
    if not dragon_name2 == "None": 
        dragon_image = Image.open(dragon[dragon_rarity2]).resize((round(400/2.1),round(480/2.1)))
        dragon_image.paste(Image.open(dragon[dragon_name2]).resize((round(400/2.1),round(480/2.1))),mask=Image.open(dragon[dragon_name2]).resize((round(400/2.1),round(480/2.1))))
        dragon_image.paste(Image.open(dragon[letter_dragon[dragon_name2]]).resize((round(114/1.6),round(101/1.6))),box=(20,150),mask=Image.open(dragon[letter_dragon[dragon_name2]]).resize((round(114/1.6),round(101/1.6))))
    elif not dragon_name3 == "None":
        dragon_image = Image.open(dragon[dragon_rarity3]).resize((round(400/2.1),round(480/2.1)))
        dragon_image.paste(Image.open(dragon[dragon_name3]).resize((round(400/2.1),round(480/2.1))),mask=Image.open(dragon[dragon_name3]).resize((round(400/2.1),round(480/2.1))))
        dragon_image.paste(Image.open(dragon[letter_dragon[dragon_name3]]).resize((round(114/1.6),round(101/1.6))),box=(20,150),mask=Image.open(dragon[letter_dragon[dragon_name3]]).resize((round(114/1.6),round(101/1.6))))
    elif not dragon_name1 == "None":
        dragon_image = Image.open(dragon[dragon_rarity1]).resize((round(400/2.1),round(480/2.1)))
        dragon_image.paste(Image.open(dragon[dragon_name1]).resize((round(400/2.1),round(480/2.1))),mask=Image.open(dragon[dragon_name1]).resize((round(400/2.1),round(480/2.1))))
        dragon_image.paste(Image.open(dragon[letter_dragon[dragon_name1]]).resize((round(114/1.6),round(101/1.6))),box=(20,150),mask=Image.open(dragon[letter_dragon[dragon_name1]]).resize((round(114/1.6),round(101/1.6))))
    else:
        dragon_image = Image.open(dragon["none"]).resize((round(400/2.1),round(480/2.1)))
    base.paste(dragon_image,mask=dragon_image,box=position['dragon_image'])
    base.paste(Image.open(button_jewel).resize((round(92*1.75),round(108*1.75))),box=position["button_jewel"],mask=Image.open(button_jewel).resize((round(92*1.75),round(108*1.75))))
    draw = ImageDraw.Draw(base)

    
    draw.multiline_text(position["lvl_weapon"],
        f"Lv.{weapon_lvl}",(255,255,255),
        anchor="mm",align="center",
        font=font_lvl)
    draw.multiline_text(position["lvl_armor"],
        f"Lv.{armor_lvl}",(255,255,255),
        anchor="mm",align="center",
        font=font_lvl)
    draw.multiline_text(position["lvl_ring1"],
        f"Lv.{ring_lvl1}",(255,255,255),
        anchor="mm",align="center",
        font=font_lvl)
    draw.multiline_text(position["lvl_ring2"],
        f"Lv.{ring_lvl2}",(255,255,255),
        anchor="mm",align="center",
        font=font_lvl)
    draw.multiline_text(position["lvl_pet1"],
        f"Lv.{pet_lvl1}",(255,255,255),
        anchor="mm",align="center",
        font=font_lvl)
    draw.multiline_text(position["lvl_pet2"],
        f"Lv.{pet_lvl2}",(255,255,255),
        anchor="mm",align="center",
        font=font_lvl)
    draw.multiline_text(position["lvl_bracelet"],
        f"Lv.{bracelet_lvl}",(255,255,255),
        anchor="mm",align="center",
        font=font_lvl)
    draw.multiline_text(position["lvl_book"],
        f"Lv.{book_lvl}",(255,255,255),
        anchor="mm",align="center",
        font=font_lvl)
    draw.multiline_text(position["lvl_locket"],
        f"Lv.{locket_lvl}",(255,255,255),
        anchor="mm",align="center",
        font=font_lvl)

    ## (from the left, from the bottom)
    if int(atk) < 1000:
        draw.text((218,1106),str(atk),(55,22,0),font=ImageFont.truetype("calculator/static/fonts/magic.otf",58))
    elif int(atk) < 10000:
        draw.text((218,1106),str(atk),(55,22,0),font=ImageFont.truetype("calculator/static/fonts/magic.otf",58))
    elif int(atk) < 100000:
        draw.text((208,1106),str(atk),(55,22,0),font=ImageFont.truetype("calculator/static/fonts/magic.otf",58))
    else:
        draw.text((198,1106),str(atk),(55,22,0),font=ImageFont.truetype("calculator/static/fonts/magic.otf",58))

    if int(pv) < 1000:
        draw.text((218,1211),str(pv),(55,22,0),font=ImageFont.truetype("calculator/static/fonts/magic.otf",58))
    elif int(pv) < 10000:
        draw.text((218,1211),str(pv),(55,22,0),font=ImageFont.truetype("calculator/static/fonts/magic.otf",58))
    elif int(pv) < 100000:
        draw.text((208,1211),str(pv),(55,22,0),font=ImageFont.truetype("calculator/static/fonts/magic.otf",58))
    elif int(pv) < 1000000:
        draw.text((198,1211),str(pv),(55,22,0),font=ImageFont.truetype("calculator/static/fonts/magic.otf",58))
    else:
        draw.text((190,1211),str(pv),(55,22,0),font=ImageFont.truetype("calculator/static/fonts/magic.otf",58))

    base.save(f"calculator/static/image/stuff_save/{pbid}.png")