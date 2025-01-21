import os
from envs.gcp_info import GCP_SPARK_MASTER_ADDRESS, GCP_DATAPROC_STOP_COMMAND, GCP_DATAPROC_START_COMMAND
from envs.server_info import DB_SERVER_ADDRESS, DB_SERVER_PASSWD, DB_SERVER_3_CONF_DIR, DB_SERVER_3_POST_DIR, DB_SERVER_2_CONF_DIR, DB_SERVER_2_POST_DIR

HOME_PATH = os.path.expanduser('~')
PROJECT_NAME = os.path.split(os.getcwd())[-1]

CONF_PATH = os.path.join(HOME_PATH, PROJECT_NAME, 'data/tuned.conf')
CONF_TMP_PATH = os.path.join(HOME_PATH, PROJECT_NAME, 'data/tuned_.conf')

# Spark ---------------------------------------
SPARK_CONF_INFO_CSV_PATH = os.path.join(HOME_PATH, PROJECT_NAME, 'data/Spark_3.1_45_parameters.csv')
SPARK_CONF_PATH = os.path.join(HOME_PATH, PROJECT_NAME, 'data/add-spark.conf')
SPARK_DEFAULT_CONF_PATH = os.path.join(HOME_PATH, PROJECT_NAME, 'data/def-spark.conf')

DATA_FOLDER_PATH = os.path.join(HOME_PATH, PROJECT_NAME, 'data')

MASTER_ADDRESS = GCP_SPARK_MASTER_ADDRESS
MASTER_CONF_PATH = os.path.join(HOME_PATH, 'HiBench/conf')
HIBENCH_REPORT_PATH = os.path.join(HOME_PATH, PROJECT_NAME, 'data/hibench.report')
# ---------------------------------------------

# PostgreSQL ----------------------------------
POSTGRES_CONF_INFO_CSV_PATH = os.path.join(HOME_PATH, PROJECT_NAME, 'data/PostgreSQL_13_112_parameters.csv')
POSTGRES_CONF_PATH = os.path.join(HOME_PATH, PROJECT_NAME, 'data/add-postgres.conf')

POSTGRES_SERVER_ADDRESS = DB_SERVER_ADDRESS
POSTGRES_SERVER_PASSWSD = DB_SERVER_PASSWD
POSTGRES_SERVER_CONF_PATH = DB_SERVER_3_CONF_DIR
POSTGRES_SERVER_POSTGRES_PATH = DB_SERVER_3_POST_DIR
POSTGRES_SERVER_2_CONF_PATH = DB_SERVER_2_CONF_DIR
POSTGRES_SERVER_2_POSTGRES_PATH = DB_SERVER_2_POST_DIR

# ---------------------------------------------

RANDOM_SEED = 1996 # TODO: Change later..

BOUNCE_PARAM = {
                "number_initial_points": 10,
                "initial_target_dimensionality": 5,
                "number_new_bins_on_split": 2,
                "maximum_number_evaluations": 50, # 200
                "batch_size" : 1,
                "results_dir" : "results",
                "maximum_number_evaluations_until_input_dim" : 50, # 100
                "dtype" : "float64",
                "use_scipy_lbfgs" : True,
            }

NOISE_PARAM = {
                "NOISY_OBSERVATIONS": 1,
                "NOISE_FREE_REPEATED_BENCHMARKING": 2,
                "NOISE_FREE_REPEATED_EXPERIMENTS": 3,
                "ADAPTIVE_NOISE": 4,
                'NOISE_MEAN': 5,
            }

TRUSTREGION_PARAM = {"length_init_discrete": 40} # 40

GP_PARAM = {
            "lengthscale_prior_shape" : 1.5, # 3
            "lengthscale_prior_rate" : 0.1, # 6
            "outputscale_prior_shape" : 1.5, # 2
            "outputscale_prior_rate" : 0.5, # 0.15
            "noise_prior_shape" : 1.1, # 1.1
            "noise_prior_rate" : 0.05 # 2
            }

BENCHMARKING_REPETITION = 3

def print_params():
    import logging
    logging.info("📢 Information of hyperparameters")
    logging.info("================================")
    logging.info("📌Environments...")
    logging.info(f"SPARK_CONF_INFO_CSV_PATH : {SPARK_CONF_INFO_CSV_PATH}")
    logging.info(f"SPARK_CONF_PATH : {SPARK_CONF_PATH}")
    logging.info(f"MASTER_ADDRESS : {MASTER_ADDRESS}")
    logging.info(f"MASTER_CONF_PATH : {MASTER_CONF_PATH}")
    logging.info(f"HIBENCH_REPORT_PATH : {HIBENCH_REPORT_PATH}")
    
    logging.info('---------------------------')
    logging.info("📌Bounce...")
    for k, v in BOUNCE_PARAM.items():
        logging.info(f"{k} : {v}")
    
    logging.info('---------------------------')
    logging.info("📌TrustRegion...")
    for k, v in TRUSTREGION_PARAM.items():
        logging.info(f"{k} : {v}")
    
    logging.info('---------------------------')
    logging.info("📌Gaussian Process...")
    for k, v in GP_PARAM.items():
        logging.info(f"{k} : {v}")
    
    logging.info("================================")