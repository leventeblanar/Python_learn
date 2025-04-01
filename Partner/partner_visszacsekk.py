

headers = {"Authorization": "ad815b38-3796-45eb-8a5c-fb935b02fe51"}
kornyezet = "p20"

## hermesbpl indulunk ki - lekérjük a PartnerQuery
## isTiltva - False - tehát ami true az ne legyen benne az eredményben
# IsTiltva = False
# D = 0
## kiszedni a környezetről a partnereket ahogy a pull_partner_telephely_ver3.py-ban
## adószám - unique - atlasDB-ből kikeressük az adószámót, ha van match
## két adószám match - külsőId passzol e az atlasos partner id-val
## Ha nem, akkor PUT