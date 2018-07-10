--------------------------------
-- Game
--------------------------------
NDefines.NGame.START_DATE = "2280.1.1"
NDefines.NGame.END_DATE = "9999.1.1"
NDefines.NGame.MAX_RANDOM_NEW_WORLD = "9999.1.1"
NDefines.NGame.GREAT_POWER_FRENZY_START = "9999.1.1"

--------------------------------
-- Compatibility / Disabled 
--------------------------------
NDefines.NNationDesigner.MANDATE_SUBCONTINENT_NAME = "west_coast_superregion"
NDefines.NDiplomacy.NUM_OF_GREAT_POWERS = 0
NDefines.NCountry.FEMALE_ADVISOR_CHANCE = 0
NDefines.NCountry.MONARCH_DEATH = 0
NDefines.NCountry.ALLOW_ZERO_BASE_VALUES = 1

--------------------------------
-- Diplomacy
--------------------------------
NDefines.NDiplomacy.STUDY_TECHNOLOGY_MIN_TECHS_AHEAD = 0 -- Allow power gain from Study Technology always

--------------------------------
-- Country
--------------------------------
NDefines.NCountry.POWER_MAX = 1000 -- Clean
NDefines.NCountry.ALLOW_ESTATE_AND_PARLIAMENT_SEAT_IN_PROVINCE = 1
NDefines.NCountry.MAX_EXTRA_PERSONALITIES = 3 -- Allow 3 modifiers
NDefines.NCountry.YEARS_PER_EXTRA_PERSONALITY = 10 
NDefines.NCountry.MAX_CROWN_COLONIES = 9999 -- Disable colonial nations
NDefines.NCountry.MIGRATION_COOLDOWN = 240 -- Slow down migration
NDefines.NCountry.INNOVATIVENESS_FIRST_REACHED_TECH_LEVEL = 5.0 -- Make innovativeness easier to gain
NDefines.NCountry.INNOVATIVENESS_FIRST_PICKED_IDEA = 5.0 -- Make innovativeness easier to gain
NDefines.NCountry.INNOVATIVENESS_BEHIND_IN_TECH_PENALTY = -0.05 -- Make it easier to lose innovativeness
NDefines.NCountry.INNOVATIVENESS_ENABLE_ANY_BEHIND_IN_TECH_PENALTY = 1 -- Make it easier to lose innovativeness
NDefines.NCountry.INNOVATIVENESS_ENABLE_PER_TECH_BEHIND_IN_TECH_PENALTY = 1 -- Make it easier to lose innovativeness
NDefines.NCountry.INNOVATIVENESS_AHEAD_OF_TIME_BONUS = 0.1 -- Make innovativeness easier to gain
NDefines.NCountry.FREE_IDEA_GROUP_COST = 1.5  -- Adapt NI unlocks to ideagroup system
NDefines.NCountry.MAX_IDEA_GROUPS_FROM_SAME_CATEGORY = 1 -- Remove ideagroup pick restriction
NDefines.NCountry.TECH_TIME_COST = 0.3	    -- tech grow with 20% cost over time.
NDefines.NCountry.TECH_AHEAD_OF_TIME = 0.1  -- per year ahead.
NDefines.NCountry.PS_ESTABLISH_SIBERIAN_FRONTIER = 50
NDefines.NCountry.PS_FACTION_BOOST = 25
NDefines.NCountry.EXPLOIT_ADM_INCOME = 120      -- Make exploit development more useful
NDefines.NCountry.EXPLOIT_DIP_SAILORS = 12      -- Make exploit development more useful
NDefines.NCountry.EXPLOIT_MIL_MANPOWER = 12     -- Make exploit development more useful
NDefines.NCountry.EXPLOIT_COOLDOWN_MONTHS = 12  -- Make exploit development more useful
NDefines.NCountry.ABDICATE_LEGITIMACY_THRESHOLD = 100 -- Allow abdication anytime
NDefines.NCountry.ABDICATE_AGE_THRESHOLD = 18 -- Allow abdication for any adult ruler
NDefines.NCountry.ABDICATE_RULING_LENGTH_THRESHOLD = 0 -- Allow abdication anytime
NDefines.NCountry.ABDICATE_LEGITIMACY_HIT = -90 -- Make abdication much more costly
NDefines.NCountry.ABDICATE_PRESTIGE_HIT = -90 -- Make abdication much more costly
NDefines.NCountry.EMBRACE_INSTITUTION_COST = 5 -- Make embracement of institutions twice as expensive
NDefines.NCountry.STATE_MAINTENANCE_DEV_FACTOR = 0.01 -- Make states more expensive to maintain
NDefines.NCountry.STATE_MAINTENANCE_CULTURE_FACTOR = 0.5 -- Make states more expensive to maintain
NDefines.NCountry.PARLIAMENT_BACKING_PERCENTAGE = 25
NDefines.NCountry.PARLIAMENT_PRESTIGE_HIT = 0
NDefines.NCountry.CULTURAL_UNION_MIN_DEV = 9999999 -- Disable cultural union (doesn't make sense with current cultures)
NDefines.NCountry.CULTURAL_UNION_MIN_RANK = -1 -- Force dev check for cultural union
NDefines.NCountry.ADVISOR_COST_INCREASE_PER_YEAR = 0 -- Disable cost increase for advisors
NDefines.NCountry.PS_REDUCE_INFLATION = 100 -- Make inflation more expensive to reduce
NDefines.NCountry.CORE_LOSE = -1 -- Cores are never lost
NDefines.NCountry.CORE_LOSE_CULTURE_GROUP = -1 -- Cores are never lost

--------------------------------
-- Economy
--------------------------------
NDefines.NEconomy.COLONIAL_MAINTENANCE_FACTOR = 2.0 -- Make colonisation cheaper
NDefines.NEconomy.BASE_INTERESTS = 10.0 -- Loans more risky in the wasteland
NDefines.NEconomy.LAND_TECH_MAINTENANCE_IMPACT = 0.05 -- 50% increase after all (20) mil techs taken
NDefines.NEconomy.DECREASE_AUTONOMY_STEP = -10  -- Make autonomy changes more gradual
NDefines.NEconomy.DECREASE_AUTONOMY_MIN = 10 
NDefines.NEconomy.INCREASE_AUTONOMY_STEP = 10 -- Make autonomy changes more gradual
NDefines.NEconomy.INCREASE_AUTONOMY_MAX = 90
NDefines.NEconomy.AUTONOMY_CHANGE_DURATION = 3650 -- Allow autonomy buttons every 10 years
NDefines.NEconomy.COLONY_MIN_AUTONOMY = 75 
NDefines.NEconomy.OVERSEAS_MIN_AUTONOMY = 50
NDefines.NEconomy.AUTONOMY_AT_CONQUEST_CLAIM = 25 -- Make claims better
NDefines.NEconomy.AUTONOMY_AT_CONQUEST = 75 -- Make unclaimed conquest worse
NDefines.NEconomy.AUTONOMY_AT_DIPLO_ANNEX = 25 -- Make diplo annex better
NDefines.NEconomy.DEBASE_ADDED_CORRUPTION = 1 -- Make debase better
NDefines.NEconomy.DEBASE_MAX_STORED_MONTHS = 1200 -- Why not?

--------------------------------
-- AI
--------------------------------
NDefines.NAI.AI_USES_HISTORICAL_IDEA_GROUPS = 0
NDefines.NAI.AI_CONVERT_CULTURES = 1   
NDefines.NAI.AGGRESSIVENESS = 500 -- Make AI more war-happy
NDefines.NAI.AGGRESSIVENESS_BONUS_EASY_WAR = 500 -- Make AI more war-happy
NDefines.NAI.NAVY_BUDGET_FRACTION = 0.2 -- Reduce AI spending on navy
NDefines.NAI.DEVELOPMENT_CAP_BASE = 30 -- Allow AI to develop more
NDefines.NAI.PEACE_TIME_MONTHS = 24 -- Reduce AI stubbornness
NDefines.NAI.PEACE_INCONCLUSIVE_THRESHOLD = 0 -- Allow for peace demands at 0
--------------------------------
-- Military 
--------------------------------
NDefines.NMilitary.COSSACKS_SHOCK_DAMAGE_BONUS = 0.1
NDefines.NMilitary.STRELTSY_FIRE_DAMAGE_BONUS = 0.1
NDefines.NMilitary.FORTRESS_COST = 0.1 -- Make forts cheaper to maintain.
NDefines.NMilitary.INFANTRY_SPEED = 1.0 -- Revert speed nerf Paradox introducted.
NDefines.NMilitary.CAVALRY_SPEED = 1.0 -- Revert speed nerf Paradox introducted.
NDefines.NMilitary.ARTILLERY_SPEED = 1.0 -- Revert speed nerf Paradox introducted.
NDefines.NMilitary.FORT_PER_DEV_RATIO = 100 -- Make army trad. from forts easier to get.
NDefines.NMilitary.MIN_MONTHLY_MANPOWER = 0.05 -- Represents difficulty in supply across wasteland
NDefines.NMilitary.MONTHLY_REINFORCE = 0.05 -- Represents difficulty in supply across wasteland
NDefines.NMilitary.WARSCORE_MAX_FROM_BATTLES = 80 -- Battles more important than capture in the wasteland
NDefines.NMilitary.NAVAL_DOCTRINE_MIN_FORCE_LIMIT = 9999 -- Disable Naval Doctrines

--------------------------------
-- GOVERNMENT
--------------------------------
NDefines.NGovernment.RUSSIAN_ABILITY_COST = 100
NDefines.NGovernment.RUSSIAN_ABILITY_POOL_SIZE = 150
NDefines.NGovernment.RUSSIAN_ABILITY_BASE_GAIN = 3

NDefines.NGovernment.RUSSIAN_ABILITY_SUBEDNIK_MIN_AUTONOMY = 10
NDefines.NGovernment.RUSSIAN_ABILITY_SUBEDNIK_AUTONOMY_CHANGE = -10
NDefines.NGovernment.RUSSIAN_ABILITY_OPRICHNINA_THRESHOLD = 0.3
NDefines.NGovernment.RUSSIAN_ABILITY_OPRICHNINA_AI_THRESHOLD = 0.85
NDefines.NGovernment.RUSSIAN_ABILITY_OPRICHNINA_CHANGE = -0.5
NDefines.NGovernment.RUSSIAN_ABILITY_STRELTSY_WE_CHANGE = -2
NDefines.NGovernment.RUSSIAN_ABILITY_STRELTSY_SPAWN_SIZE = 0.5

NDefines.NGovernment.IQTA_POLICY_COOLDOWN_YEARS = 20
NDefines.NGovernment.EFFICIENT_FARMING_DUCAT_MULTIPLIER = 2
NDefines.NGovernment.LAND_AQUISITION_MANPOWER_MULTIPLIER = 0.05

NDefines.NGovernment.SEIZE_CLERICAL_HOLDINGS_COST = 100
NDefines.NGovernment.INVITE_MINORITIES_COST = 100
NDefines.NGovernment.SANCTION_HOLY_WAR_COST = 100
NDefines.NGovernment.FEUDAL_THEOCRACY_INTERACTION_COOLDOWN_YEARS = 5
NDefines.NGovernment.SANCTION_HOLY_WAR_LIST_SIZE = 7
NDefines.NGovernment.INVITE_MINORITIES_GAIN = 1

NDefines.NGovernment.MAMLUK_ABILITY_POOL_SIZE = 150
NDefines.NGovernment.MAMLUK_ABILITY_COST = 100
NDefines.NGovernment.MAMLUK_RECRUIT_MANPOWER_MULTIPLIER = 100
NDefines.NGovernment.MAMLUK_SELL_SLAVES_DUCATS_MULTIPLIER = 10
NDefines.NGovernment.PROMOTE_MAMLUK_CULTURE_DURATION_YEARS = 1

NDefines.NGovernment.TRAIN_HORSEMANSHIP_DURATION_YEARS = 5
NDefines.NGovernment.CONSCRIPT_FROM_TRIBES_AMOUNT = 5
NDefines.NGovernment.CONSCRIPT_FROM_TRIBES_TIME = 0.25
NDefines.NGovernment.TRIBAL_ALLEGIANCE_MAX = 100
NDefines.NGovernment.TRIBAL_ALLEGIANCE_HUMILIATE = 30.0
NDefines.NGovernment.TRIBAL_FEDERATION_ABILITY_COST = 50
NDefines.NGovernment.ENLIST_GENERAL_TRADITION = 50

--------------------------------
-- RELIGION
--------------------------------
-- Piety
NDefines.NReligion.PIETY_CORRUPTION = -2
NDefines.NReligion.PIETY_MANPOWER = 2.0
NDefines.NReligion.PIETY_COST = 0.5
NDefines.NReligion.PIETY_ABS_THRESHOLD = 0.75
NDefines.NReligion.PIETY_ACTION_COOLDOWN = 5

-- Schools
NDefines.NReligion.NOT_SAME_MUSLIM_SCHOOL_ALLIANCE_ACCEPTANCE = 15
NDefines.NReligion.NOT_SAME_MUSLIM_SCHOOL_ROYAL_MARRIAGE_ACCEPTANCE = 15
NDefines.NReligion.SAME_MUSLIM_SCHOOL_ALLIANCE_ACCEPTANCE = 15
NDefines.NReligion.SAME_MUSLIM_SCHOOL_ROYAL_MARRIAGE_ACCEPTANCE = 15

-- Orthodox Icons ()
NDefines.NReligion.CONSECRATE_PATRIACH_AUTHORITY_BOOST = 0.1   --5% or so
NDefines.NReligion.CONSECRATE_PATRIARCH_THRESHOLD = 10          --in development
NDefines.NReligion.ORTHODOX_ICON_DURATION_MONTHS = 240
NDefines.NReligion.ORTHODOX_ICON_AUTHORITY_COST = 0.5

-- Religious Reforms ()
NDefines.NReligion.MAYA_COLLAPSE_PROVINCES = 10	            -- Maya collapses to this size on reform
NDefines.NReligion.MAYA_COLLAPSE_PROVINCES_PER_REFORM = 2   -- Maya keeps this many extra provinces per reform

-- Doom ()
NDefines.NReligion.YEARLY_DOOM_INCREASE = 1             -- Multiplied by number of provinces
NDefines.NReligion.DOOM_REDUCTION_FROM_REFORMS = 0.2    -- This much less monthly doom (as a fraction of whole) for each reform passed
NDefines.NReligion.DOOM_REDUCTION_FROM_OCCUPATION = 0.05-- Multiplied by development
NDefines.NReligion.DOOM_REDUCTION_FROM_BATTLE = 1       -- Per 1000 men killed
NDefines.NReligion.DOOM_REDUCTION_FROM_SACRIFICE = 1    -- Multiplied by power
NDefines.NReligion.SACRIFICE_COOLDOWN = 3               -- Years before you can sacrifice a ruler/heir from same country
	
-- Authority
NDefines.NReligion.SACRIFICE_LIBERTY_DESIRE = 25        -- LD added from sacrifice (ruler)
NDefines.NReligion.SACRIFICE_LIBERTY_DESIRE_HEIR = 20   -- LD added from sacrifice (heir)
NDefines.NReligion.AUTHORITY_FROM_DEVELOPMENT = 0.02	-- Multiplied by development (affected by autonomy)
NDefines.NReligion.AUTHORITY_FROM_AUTONOMY = 0.2        -- Authority loss from granting autonomy

-- Papacy
NDefines.NReligion.MIN_CARDINALS = 0   
NDefines.NReligion.MAX_CARDINALS = 0   
NDefines.NReligion.MAX_CARDINALS_PER_COUNTRY = 0   
NDefines.NReligion.NUMBER_OF_POSSIBLE_CARDINALS = 0 
NDefines.NReligion.YEARLY_PAPAL_INFLUENCE_CATHOLIC = 1
NDefines.NReligion.MAX_PAPAL_INFLUENCE = 500

-- Church Aspects
NDefines.NReligion.ASPECT_ADD_COST = 100            -- Cost in Church Power to remove an Aspect of Faith.
NDefines.NReligion.ASPECT_REMOVE_COST = 0           -- Stabhit for removing an Aspect of Faith.
NDefines.NReligion.MAX_UNLOCKED_ASPECTS = 3         -- Maximum number of Aspects of Faith the player can have unlocked at once.
NDefines.NReligion.CHURCH_POWER_RATE_SCALE = 0.1    -- Scaling value for rate at which church power is gained.

-- Karma
NDefines.NReligion.KARMA_FOR_OFFENSIVE_WAR = -10
NDefines.NReligion.KARMA_FOR_DEFENSIVE_WAR = 10
NDefines.NReligion.KARMA_FOR_HONORING_CTA = 25
NDefines.NReligion.KARMA_PER_RELEASED_PROVINCE = 1
NDefines.NReligion.KARMA_PER_TAKEN_PROVINCE = -1
NDefines.NReligion.KARMA_TOO_HIGH = 33
NDefines.NReligion.KARMA_TOO_LOW = -33
NDefines.NReligion.KARMA_JUST_RIGHT_HIGH = 33
NDefines.NReligion.KARMA_JUST_RIGHT_LOW = -33
NDefines.NReligion.KARMA_RESTORE_ON_RULER_DEATH = 25
    
-- Secondary
NDefines.NReligion.CHANGE_SECONDARY_PRESTIGE_HIT = -50

-- Harmony
NDefines.NReligion.MIN_HARMONIZE_DEVELOPMENT = 20
NDefines.NReligion.STARTING_HARMONY = 50.0          -- Confucian countries start with this.
NDefines.NReligion.YEARLY_HARMONY_INCREASE = 1.0
NDefines.NReligion.HARMONY_LOSS_PER_DEV_CONVERTED = 1.0
NDefines.NReligion.YEARLY_HARMONY_INCREASE_WHEN_HARMONIZING = -3.0
NDefines.NReligion.YEARLY_HARMONIZATION_PROGRESS = 0.03 
    
-- Isolationism
NDefines.NReligion.INITIAL_ISOLATIONISM = 1	-- Level of isolationism for a newly shintoed country.

--------------------------------
-- Graphics
--------------------------------
NDefines.NGraphics.SHOW_MONTHLY_TAX_INCOME = 1

