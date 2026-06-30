"""
SDP Builder — PySpark pipelines (dp) for `new_pipeline_test`

Requires a Lakeflow / PySpark pipelines context with `spark` and `dp` available.
"""

from pyspark import pipelines as dp

# --- john_snow_labs_occupational_health_and_safety.occupational_health_and_safety.us_bureau_of_labor_statistics_injury_and_illness_data_by_industry (logical projection via transformation SQL; base table john_snow_labs_occupational_health_and_safety.occupational_health_and_safety.us_bureau_of_labor_statistics_injury_and_illness_data_by_industry) ---
# Target UC namespace (defaults + overrides): classic_stable_kremer_catalog.silver_test
# Declarative table (no primary keys): `classic_stable_kremer_catalog.silver_test.us_bureau_of_labor_statistics_injury_and_illness_data_by_industry` — @dp.table; Python def `us_bureau_of_labor_statistics_injury_and_illness_data_by_industry`

@dp.table(name="classic_stable_kremer_catalog.silver_test.us_bureau_of_labor_statistics_injury_and_illness_data_by_industry")
def us_bureau_of_labor_statistics_injury_and_illness_data_by_industry():
    return spark.sql("""
SELECT
  `North_American_Industry_Classification_2012` AS north_american_industry_classification_2012,
  `North_American_Industry_Classification_Codes_2012` AS north_american_industry_classification_codes_2012,
  `Classification_Hierarchical_Level` AS classification_hierarchical_level,
  `Measures` AS measures,
  `Total_Recordable_Cases` AS total_recordable_cases,
  `Cases_With_Days_Away_From_Work` AS cases_with_days_away_from_work,
  `Cases_With_Job_Transfer_Or_Restriction` AS cases_with_job_transfer_or_restriction,
  `Total_With_Days_Away_From_Work_Or_Job_Transfer_Or_Restriction` AS total_with_days_away_from_work_or_job_transfer_or_restriction,
  `Other_Recordable_Cases` AS other_recordable_cases,
  `Is_Divided_By_1000` AS is_divided_by_1000,
  `Is_Excludes_Farms` AS is_excludes_farms
FROM
`john_snow_labs_occupational_health_and_safety`.`occupational_health_and_safety`.`us_bureau_of_labor_statistics_injury_and_illness_data_by_industry`
""")

# --- john_snow_labs_occupational_health_and_safety.occupational_health_and_safety.lost_time_injuries_frequency_by_industry_in_uk (logical projection via transformation SQL; base table john_snow_labs_occupational_health_and_safety.occupational_health_and_safety.lost_time_injuries_frequency_by_industry_in_uk) ---
# Target UC namespace (defaults + overrides): classic_stable_kremer_catalog.silver_test
# Declarative table (no primary keys): `classic_stable_kremer_catalog.silver_test.lost_time_injuries_frequency_by_industry_in_uk` — @dp.table; Python def `lost_time_injuries_frequency_by_industry_in_uk`

@dp.table(name="classic_stable_kremer_catalog.silver_test.lost_time_injuries_frequency_by_industry_in_uk")
def lost_time_injuries_frequency_by_industry_in_uk():
    return spark.sql("""
SELECT
  `Measurement_Period_Type` AS measurement_period_type,
  `Injuries_By_Days_Of_Absence_From_Work` AS injuries_by_days_of_absence_from_work,
  `SIC_Level` AS sic_level,
  `SIC_Section_Code` AS sic_section_code,
  `Industry` AS industry,
  `SIC_Code` AS sic_code,
  `Measurement_Period` AS measurement_period,
  `Cases` AS cases,
  `Cases_Confidence_Interval_Low` AS cases_confidence_interval_low,
  `Cases_Confidence_Interval_High` AS cases_confidence_interval_high,
  `Rate` AS rate,
  `Rate_Confidence_Interval_Low` AS rate_confidence_interval_low,
  `Rate_Confidence_Interval_High` AS rate_confidence_interval_high,
  `Significance_Level_Different_To_All_Industries_Rate` AS significance_level_different_to_all_industries_rate,
  `Significance_Level_Different_To_Previous_Period_Rate` AS significance_level_different_to_previous_period_rate,
  `Is_Rate_Estimated_On_Less_Than_30_Values` AS is_rate_estimated_on_less_than_30_values
FROM
`john_snow_labs_occupational_health_and_safety`.`occupational_health_and_safety`.`lost_time_injuries_frequency_by_industry_in_uk`
""")
