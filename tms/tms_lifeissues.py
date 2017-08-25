
from tms.tms_class import TMSPack, TMSVerse

LIFE_ISSUES_ANGER_KEY = "Anger"
LIFE_ISSUES_SIN_KEY = "Sin"
LIFE_ISSUES_DEPRESSION_KEY = "Depression"
LIFE_ISSUES_GUILT_KEY = "Guilt"
LIFE_ISSUES_GODSWILL_KEY = "God's Will"
LIFE_ISSUES_LOVE_KEY = "Love"
LIFE_ISSUES_MONEY_KEY = "Money"
LIFE_ISSUES_PERFECTIONISM_KEY = "Perfectionism"
LIFE_ISSUES_SELFIMAGE_KEY = "Self-Image"
LIFE_ISSUES_SEX_KEY = "Sex"
LIFE_ISSUES_STRESS_KEY = "Stress"
LIFE_ISSUES_SUFFERING_KEY = "Suffering"

def keys():
    return [ 
        LIFE_ISSUES_ANGER_KEY,
        LIFE_ISSUES_SIN_KEY,
        LIFE_ISSUES_DEPRESSION_KEY,
        LIFE_ISSUES_GUILT_KEY,
        LIFE_ISSUES_GODSWILL_KEY,
        LIFE_ISSUES_LOVE_KEY,
        LIFE_ISSUES_MONEY_KEY,
        LIFE_ISSUES_PERFECTIONISM_KEY,
        LIFE_ISSUES_SELFIMAGE_KEY,
        LIFE_ISSUES_SEX_KEY,
        LIFE_ISSUES_STRESS_KEY,
        LIFE_ISSUES_SUFFERING_KEY
    ]

ANGER_ALIASES = ["Anger", "Rage", "Wrath", "Angry", "Angered", "Furious"]
ANGER_PACK = [
    TMSVerse(LIFE_ISSUES_ANGER_KEY,        "Anger",        1,     "Proverbs 15 : 1", 
                                    ["Gentle", "Wrath", "Harsh", "Word"]),
    TMSVerse(LIFE_ISSUES_ANGER_KEY,        "Anger",        2,     "Proverbs 29 : 11", 
                                    ["Fool", "Vent", "Wise", "Withhold"]),
    TMSVerse(LIFE_ISSUES_ANGER_KEY,        "Anger",        3,     "Romans 12 : 19", 
                                    ["Vengeance", "Revenge", "Wrath", "God"]),
    TMSVerse(LIFE_ISSUES_ANGER_KEY,        "Anger",        4,     "Ephesians 4 : 26 - 27", 
                                    ["Day", "Sin", "Opportunity", "Devil"]),
    TMSVerse(LIFE_ISSUES_ANGER_KEY,        "Anger",        5,     "Colossians 3 : 8 - 10", 
                                    ["Wrath", "Malice", "Old", "New", "Self"]),
    TMSVerse(LIFE_ISSUES_ANGER_KEY,        "Anger",        6,     "James 1 : 19 - 20", 
                                    ["Listen", "Speak", "Angry", "Quick"])
]

SIN_ALIASES = ["Sin", "Wrong", "Wrongdoing", "Disobedience", "Sinful", "Wickedness"]
SIN_PACK = [
    TMSVerse(LIFE_ISSUES_SIN_KEY,        "Sin",          1,     "Romans 6 : 11 - 13", 
                                    ["Dead", "Alive", "Reign", "Obey", "Righteousness"]),
    TMSVerse(LIFE_ISSUES_SIN_KEY,        "Sin",          2,     "1 Corinthians 10 : 13", 
                                    ["Temptation", "Faithful", "Tempted", "Victory"]),
    TMSVerse(LIFE_ISSUES_SIN_KEY,        "Sin",          3,     "Galatians 6 : 1 - 2", 
                                    ["Transgression", "Gentleness", "Tempted", "Burdens"]),
    TMSVerse(LIFE_ISSUES_SIN_KEY,        "Sin",          4,     "Ephesians 6 : 10 - 12", 
                                    ["Strong", "Armor", "Evil", "Spiritual"]),
    TMSVerse(LIFE_ISSUES_SIN_KEY,        "Sin",          5,     "James 4 : 7 - 8", 
                                    ["Submit", "Resist", "Devil", "Flee", "Cleanse"]),
    TMSVerse(LIFE_ISSUES_SIN_KEY,        "Sin",          6,     "1 John 1 : 8", 
                                    ["Deceive", "Truth", "Blameless", "Say"]),
    TMSVerse(LIFE_ISSUES_SIN_KEY,        "Sin",          7,     "1 John 1 : 9", 
                                    ["Confess", "Faithful", "Just", "Forgive", "Cleanse"])
]

DEPRESSION_ALIASES = ["Depression", "Depressed", "Depressing", "Sadness", "Sad", "Sorrow"]
DEPRESSION_PACK = [
    TMSVerse(LIFE_ISSUES_DEPRESSION_KEY,    "Depression",      1,   "Isaiah 43 : 1 - 3", 
                                    []),
    TMSVerse(LIFE_ISSUES_DEPRESSION_KEY,    "Depression",      2,   "2 Corinthians 4 : 7 - 10", 
                                    []),
    TMSVerse(LIFE_ISSUES_DEPRESSION_KEY,    "Depression",      3,   "Psalm 42 : 5", 
                                    []),
    TMSVerse(LIFE_ISSUES_DEPRESSION_KEY,    "Depression",      4,   "Psalm 34 : 17 - 18", 
                                    []),
    TMSVerse(LIFE_ISSUES_DEPRESSION_KEY,    "Depression",      5,   "Lamentations 3 : 19 - 23", 
                                    []),
    TMSVerse(LIFE_ISSUES_DEPRESSION_KEY,    "Depression",      6,   "2 Corinthians 1 : 8 - 9", 
                                    [])
]

GUILT_ALIASES = ["Guilt", "Guilty", "Conscience", "Forgive", "Forgiveness", "Forgiven"]
GUILT_PACK = [
    TMSVerse(LIFE_ISSUES_GUILT_KEY,        "Guilt",        1,     "Psalm 32 : 1 - 2",           GUILT_ALIASES),
    TMSVerse(LIFE_ISSUES_GUILT_KEY,        "Guilt",        2,     "Psalm 51 : 9 - 10",          GUILT_ALIASES),
    TMSVerse(LIFE_ISSUES_GUILT_KEY,        "Guilt",        3,     "Proverbs 28 : 13",           GUILT_ALIASES),
    TMSVerse(LIFE_ISSUES_GUILT_KEY,        "Guilt",        4,     "Romans 8 : 1 - 2",           GUILT_ALIASES),
    TMSVerse(LIFE_ISSUES_GUILT_KEY,        "Guilt",        5,     "2 Corinthians 7 : 10",       GUILT_ALIASES),
    TMSVerse(LIFE_ISSUES_GUILT_KEY,        "Guilt",        6,     "James 5 : 16",               GUILT_ALIASES)
]

GODSWILL_ALIASES = ["God's Will", "Will of God", "Will", "Sovereignty", "God's Plan", "God"]
GODSWILL_PACK = [
    TMSVerse(LIFE_ISSUES_GODSWILL_KEY,        "God's Will",       1,  "Proverbs 3 : 5 - 6",     GODSWILL_ALIASES),
    TMSVerse(LIFE_ISSUES_GODSWILL_KEY,        "God's Will",       2,  "Proverbs 3 : 7",         GODSWILL_ALIASES),
    TMSVerse(LIFE_ISSUES_GODSWILL_KEY,        "God's Will",       3,  "Proverbs 16 : 9",        GODSWILL_ALIASES),
    TMSVerse(LIFE_ISSUES_GODSWILL_KEY,        "God's Will",       4,  "Isaiah 30 : 21",         GODSWILL_ALIASES),
    TMSVerse(LIFE_ISSUES_GODSWILL_KEY,        "God's Will",       5,  "Jeremiah 29 : 11 - 13",  GODSWILL_ALIASES),
    TMSVerse(LIFE_ISSUES_GODSWILL_KEY,        "God's Will",       6,  "Romans 12 : 1 - 2",      GODSWILL_ALIASES),
    TMSVerse(LIFE_ISSUES_GODSWILL_KEY,        "God's Will",       7,  "1 John 5 : 14 - 15",     GODSWILL_ALIASES)
]

LOVE_ALIASES = ["Love", "Loving", "Agape", "Storge", "Eros", "Phileo"]
LOVE_PACK = [
    TMSVerse(LIFE_ISSUES_LOVE_KEY,        "Love",         1,     "Matthew 22 : 37 - 40",        LOVE_ALIASES),
    TMSVerse(LIFE_ISSUES_LOVE_KEY,        "Love",         2,     "John 13 : 34 - 35",           LOVE_ALIASES),
    TMSVerse(LIFE_ISSUES_LOVE_KEY,        "Love",         3,     "Romans 8 : 38 - 39",          LOVE_ALIASES),
    TMSVerse(LIFE_ISSUES_LOVE_KEY,        "Love",         4,     "1 Corinthians 13 : 1 - 3",    LOVE_ALIASES),
    TMSVerse(LIFE_ISSUES_LOVE_KEY,        "Love",         5,     "1 Corinthians 13 : 4 - 8",    LOVE_ALIASES),
    TMSVerse(LIFE_ISSUES_LOVE_KEY,        "Love",         6,     "1 John 4 : 20",               LOVE_ALIASES)
]

MONEY_ALIASES = ["Money", "Wealth", "Riches", "Rich", "Wealthy", "Prosperous"]
MONEY_PACK = [
    TMSVerse(LIFE_ISSUES_MONEY_KEY,        "Money",        1,     "Deuteronomy 8 : 17 - 18",    MONEY_ALIASES),
    TMSVerse(LIFE_ISSUES_MONEY_KEY,        "Money",        2,     "Proverbs 3 : 9 - 10",        MONEY_ALIASES),
    TMSVerse(LIFE_ISSUES_MONEY_KEY,        "Money",        3,     "Matthew 6 : 19 - 21",        MONEY_ALIASES),
    TMSVerse(LIFE_ISSUES_MONEY_KEY,        "Money",        4,     "Matthew 6 : 24",             MONEY_ALIASES),
    TMSVerse(LIFE_ISSUES_MONEY_KEY,        "Money",        5,     "Philippians 4 : 11 - 13",    MONEY_ALIASES),
    TMSVerse(LIFE_ISSUES_MONEY_KEY,        "Money",        6,     "1 Timothy 6 : 9 - 10",       MONEY_ALIASES)
]

PERFECTIONISM_ALIASES = ["Perfectionism", "Perfect", "Perfection", "Salvation", "Achievements", "Grace"]
PERFECTIONISM_PACK = [
    TMSVerse(LIFE_ISSUES_PERFECTIONISM_KEY,        "Perfectionism",    1,  "Psalm 127 : 1 - 2",         PERFECTIONISM_ALIASES),
    TMSVerse(LIFE_ISSUES_PERFECTIONISM_KEY,        "Perfectionism",    2,  "Ecclesiastes 2 : 10 - 11",  PERFECTIONISM_ALIASES),
    TMSVerse(LIFE_ISSUES_PERFECTIONISM_KEY,        "Perfectionism",    3,  "Luke 10 : 40 - 42",         PERFECTIONISM_ALIASES),
    TMSVerse(LIFE_ISSUES_PERFECTIONISM_KEY,        "Perfectionism",    4,  "2 Corinthians 12 : 9",      PERFECTIONISM_ALIASES),
    TMSVerse(LIFE_ISSUES_PERFECTIONISM_KEY,        "Perfectionism",    5,  "Galatians 3 : 3",           PERFECTIONISM_ALIASES),
    TMSVerse(LIFE_ISSUES_PERFECTIONISM_KEY,        "Perfectionism",    6,  "Ephesians 2 : 8 - 9",       PERFECTIONISM_ALIASES)
]

SELFIMAGE_ALIASES = ["Self Image", "Self", "Self Worth", "Self Esteem", "Confidence", "Self Pity"]
SELFIMAGE_PACK = [
    TMSVerse(LIFE_ISSUES_SELFIMAGE_KEY,        "Self-Image",       1,  "1 Samuel 16 : 7",           SELFIMAGE_ALIASES),
    TMSVerse(LIFE_ISSUES_SELFIMAGE_KEY,        "Self-Image",       2,  "Psalm 139 : 13 - 14",       SELFIMAGE_ALIASES),
    TMSVerse(LIFE_ISSUES_SELFIMAGE_KEY,        "Self-Image",       3,  "Jeremiah 9 : 23 - 24",      SELFIMAGE_ALIASES),
    TMSVerse(LIFE_ISSUES_SELFIMAGE_KEY,        "Self-Image",       4,  "Matthew 10 : 29 - 31",      SELFIMAGE_ALIASES),
    TMSVerse(LIFE_ISSUES_SELFIMAGE_KEY,        "Self-Image",       5,  "Philippians 2 : 3 - 11",    SELFIMAGE_ALIASES),
    TMSVerse(LIFE_ISSUES_SELFIMAGE_KEY,        "Self-Image",       6,  "1 Peter 3 : 3 - 4",         SELFIMAGE_ALIASES)
]

SEX_ALIASES = ["Sex", "Sexuality", "Body", "Intimacy", "Physical Intimacy", "Intimate"]
SEX_PACK = [
    TMSVerse(LIFE_ISSUES_SEX_KEY,        "Sex",         1,      "Matthew 5 : 27 - 28",          SEX_ALIASES),
    TMSVerse(LIFE_ISSUES_SEX_KEY,        "Sex",         2,      "Romans 13 : 13 - 14",          SEX_ALIASES),
    TMSVerse(LIFE_ISSUES_SEX_KEY,        "Sex",         3,      "1 Corinthians 6 : 18 - 20",    SEX_ALIASES),
    TMSVerse(LIFE_ISSUES_SEX_KEY,        "Sex",         4,      "Ephesians 5 : 3",              SEX_ALIASES),
    TMSVerse(LIFE_ISSUES_SEX_KEY,        "Sex",         5,      "1 Thessalonians 4 : 3 - 5",    SEX_ALIASES),
    TMSVerse(LIFE_ISSUES_SEX_KEY,        "Sex",         6,      "Hebrews 13 : 4",               SEX_ALIASES)
]

STRESS_ALIASES = ["Stress", "Stressful", "Pressure", "Burden", "Worry", "Anxiety"]
STRESS_PACK = [
    TMSVerse(LIFE_ISSUES_STRESS_KEY,        "Stress",           1,  "Psalm 73 : 26",                STRESS_ALIASES),
    TMSVerse(LIFE_ISSUES_STRESS_KEY,        "Stress",           2,  "Psalm 118 : 5 - 6",            STRESS_ALIASES),
    TMSVerse(LIFE_ISSUES_STRESS_KEY,        "Stress",           3,  "Matthew 11 : 28 - 30",         STRESS_ALIASES),
    TMSVerse(LIFE_ISSUES_STRESS_KEY,        "Stress",           4,  "2 Corinthians 4 : 16 - 18",    STRESS_ALIASES),
    TMSVerse(LIFE_ISSUES_STRESS_KEY,        "Stress",           5,  "Philippians 4 : 6 - 7",        STRESS_ALIASES),
    TMSVerse(LIFE_ISSUES_STRESS_KEY,        "Stress",           6,  "1 Peter 5 : 5 - 7",            STRESS_ALIASES)
]

SUFFERING_ALIASES = ["Suffering", "Suffer", "Pain", "Enduring", "Agony", "Comfort"]
SUFFERING_PACK = [
    TMSVerse(LIFE_ISSUES_SUFFERING_KEY,        "Suffering",        1,  "Romans 5 : 2 - 5",          SUFFERING_ALIASES),
    TMSVerse(LIFE_ISSUES_SUFFERING_KEY,        "Suffering",        2,  "2 Corinthians 1 : 3 - 4",   SUFFERING_ALIASES),
    TMSVerse(LIFE_ISSUES_SUFFERING_KEY,        "Suffering",        3,  "James 1 : 2 - 4",           SUFFERING_ALIASES),
    TMSVerse(LIFE_ISSUES_SUFFERING_KEY,        "Suffering",        4,  "James 1 : 12",              SUFFERING_ALIASES),
    TMSVerse(LIFE_ISSUES_SUFFERING_KEY,        "Suffering",        5,  "1 Peter 1 : 6 - 7",         SUFFERING_ALIASES),
    TMSVerse(LIFE_ISSUES_SUFFERING_KEY,        "Suffering",        6,  "1 Peter 4 : 12 - 13",       SUFFERING_ALIASES)
]


def data():
    return {
        LIFE_ISSUES_ANGER_KEY :             ANGER_PACK,
        LIFE_ISSUES_SIN_KEY :               SIN_PACK,
        LIFE_ISSUES_DEPRESSION_KEY :        DEPRESSION_PACK,
        LIFE_ISSUES_GUILT_KEY :             GUILT_PACK,
        LIFE_ISSUES_GODSWILL_KEY :          GODSWILL_PACK,
        LIFE_ISSUES_LOVE_KEY :              LOVE_PACK,
        LIFE_ISSUES_MONEY_KEY :             MONEY_PACK,
        LIFE_ISSUES_PERFECTIONISM_KEY :     PERFECTIONISM_PACK,
        LIFE_ISSUES_SELFIMAGE_KEY :         SELFIMAGE_PACK,
        LIFE_ISSUES_SEX_KEY :               SEX_PACK,
        LIFE_ISSUES_STRESS_KEY :            STRESS_PACK,
        LIFE_ISSUES_SUFFERING_KEY :         SUFFERING_PACK
    }

def names():
    return {
        LIFE_ISSUES_ANGER_KEY :             "Life Issues: Anger",
        LIFE_ISSUES_SIN_KEY :               "Life Issues: Sin",
        LIFE_ISSUES_DEPRESSION_KEY :        "Life Issues: Depression",
        LIFE_ISSUES_GUILT_KEY :             "Life Issues: Guilt",
        LIFE_ISSUES_GODSWILL_KEY :          "Life Issues: God's Will",
        LIFE_ISSUES_LOVE_KEY :              "Life Issues: Love",
        LIFE_ISSUES_MONEY_KEY :             "Life Issues: Money",
        LIFE_ISSUES_PERFECTIONISM_KEY :     "Life Issues: Perfectionism",
        LIFE_ISSUES_SELFIMAGE_KEY :         "Life Issues: Self-Image",
        LIFE_ISSUES_SEX_KEY :               "Life Issues: Sex",
        LIFE_ISSUES_STRESS_KEY :            "Life Issues: Stress",
        LIFE_ISSUES_SUFFERING_KEY :         "Life Issues: Suffering"
    }

def aliases():
    return {
        LIFE_ISSUES_ANGER_KEY :             ANGER_ALIASES,
        LIFE_ISSUES_SIN_KEY :               SIN_ALIASES,
        LIFE_ISSUES_DEPRESSION_KEY :        DEPRESSION_ALIASES,
        LIFE_ISSUES_GUILT_KEY :             GUILT_ALIASES,
        LIFE_ISSUES_GODSWILL_KEY :          GODSWILL_ALIASES,
        LIFE_ISSUES_LOVE_KEY :              LOVE_ALIASES,
        LIFE_ISSUES_MONEY_KEY :             MONEY_ALIASES,
        LIFE_ISSUES_PERFECTIONISM_KEY :     PERFECTIONISM_ALIASES,
        LIFE_ISSUES_SELFIMAGE_KEY :         SELFIMAGE_ALIASES,
        LIFE_ISSUES_SEX_KEY :               SEX_ALIASES,
        LIFE_ISSUES_STRESS_KEY :            STRESS_ALIASES,
        LIFE_ISSUES_SUFFERING_KEY :         SUFFERING_ALIASES
    }

def top():
    return LIFE_ISSUES_ANGER_KEY

LIFE_ISSUES_PACK = TMSPack(keys(), data(), names(), aliases(), top())
def pack():
    return LIFE_ISSUES_PACK