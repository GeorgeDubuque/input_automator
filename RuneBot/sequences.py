
# Smelt Iron in Falador

smelt_list = ["falIronBar", "falIronBar1"]
fal_to_bank_list = ["falFurnToBank", "falFurnToBank1"]
dep_half_list = ["depositHalf", "depositHalf1", "depositHalf2"]
with_iron_list = ["withIon", "withIon1", "withIon2", "withIon3", "withIon4"]
to_furn_list = ["falBankToFurnace", "falBankToFurnace1", "falBankToFurnace2"]

smelt_sequence = [with_iron_list, to_furn_list, smelt_list, fal_to_bank_list, dep_half_list]


# Mine Iron Ore in Varrock

mine_list = ["mineIron"]
var_to_bank_list = ["mtb", "mtb1", "mtb2", "mtb3", "mtb4", "mtb5", "mtb6"]
to_mine_list = ["btm", "btm1"]
deposit_list = ["depAll", "depAll1", "depAll2", "depAll3", "depAll4"]


mine_iron_sequence = [mine_list, var_to_bank_list, deposit_list, to_mine_list]


# Mine Coal in Barbarian Village

mine_list = ["mineCoal", "mineCoal1", "mineCoal2", "mineCoal3"]
fal_to_bank_list = ["falMineToBank", "falMineToBank1", "falMineToBank2", "falMineToBank3"]
fal_to_mine_list = ["falBankToMine", "falBankToMine1", "falBankToMine2", "falBankToMine3"]

mine_coal_sequence = [mine_list, fal_to_bank_list, deposit_list, fal_to_mine_list]


# Sell Iron Bar

with_iron_bar_list = ["with_iron_bar"]
move_gx_list = ["moveToGX"]
offer_list = ["offerAll"]
move_bank_list = ["moveToBank"]

sell_shit = ["sell_iron_ore", "sell_iron_ore1"]

sell_iron_bar_sequence = [sell_shit]
