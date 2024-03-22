{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "104f845b",
   "metadata": {
    "papermill": {
     "duration": 0.01143,
     "end_time": "2023-09-16T09:19:42.711115",
     "exception": false,
     "start_time": "2023-09-16T09:19:42.699685",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Online Payments Fraud Detection\n",
    "\n",
    "This notebook includes **Logistic Regression, Decision Tree, Random Forest, Gradient Boosting** classification models and accuracy scores.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "698422fe",
   "metadata": {
    "papermill": {
     "duration": 0.461631,
     "end_time": "2023-09-16T09:19:43.183876",
     "exception": false,
     "start_time": "2023-09-16T09:19:42.722245",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# # This Python 3 environment comes with many helpful analytics libraries installed\n",
    "# # It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python\n",
    "# # For example, here's several helpful packages to load\n",
    "\n",
    "# import numpy as np # linear algebra\n",
    "# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n",
    "\n",
    "# # Input data files are available in the read-only \"../input/\" directory\n",
    "# # For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory\n",
    "\n",
    "# import os\n",
    "# for dirname, _, filenames in os.walk('/kaggle/input'):\n",
    "#     for filename in filenames:\n",
    "#         print(os.path.join(dirname, filename))\n",
    "\n",
    "# # You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using \"Save & Run All\" \n",
    "# # You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5bc9a081",
   "metadata": {
    "papermill": {
     "duration": 0.01115,
     "end_time": "2023-09-16T09:19:43.206577",
     "exception": false,
     "start_time": "2023-09-16T09:19:43.195427",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Understanding Data & Preprocessing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9f5f05f1",
   "metadata": {
    "papermill": {
     "duration": 1.809612,
     "end_time": "2023-09-16T09:19:45.027384",
     "exception": false,
     "start_time": "2023-09-16T09:19:43.217772",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "055377b0",
   "metadata": {
    "papermill": {
     "duration": 22.423372,
     "end_time": "2023-09-16T09:20:07.462265",
     "exception": false,
     "start_time": "2023-09-16T09:19:45.038893",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>step</th>\n",
       "      <th>type</th>\n",
       "      <th>amount</th>\n",
       "      <th>nameOrig</th>\n",
       "      <th>oldbalanceOrg</th>\n",
       "      <th>newbalanceOrig</th>\n",
       "      <th>nameDest</th>\n",
       "      <th>oldbalanceDest</th>\n",
       "      <th>newbalanceDest</th>\n",
       "      <th>isFraud</th>\n",
       "      <th>isFlaggedFraud</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>PAYMENT</td>\n",
       "      <td>9839.64</td>\n",
       "      <td>C1231006815</td>\n",
       "      <td>170136.0</td>\n",
       "      <td>160296.36</td>\n",
       "      <td>M1979787155</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>PAYMENT</td>\n",
       "      <td>1864.28</td>\n",
       "      <td>C1666544295</td>\n",
       "      <td>21249.0</td>\n",
       "      <td>19384.72</td>\n",
       "      <td>M2044282225</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>TRANSFER</td>\n",
       "      <td>181.00</td>\n",
       "      <td>C1305486145</td>\n",
       "      <td>181.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C553264065</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>CASH_OUT</td>\n",
       "      <td>181.00</td>\n",
       "      <td>C840083671</td>\n",
       "      <td>181.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C38997010</td>\n",
       "      <td>21182.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>PAYMENT</td>\n",
       "      <td>11668.14</td>\n",
       "      <td>C2048537720</td>\n",
       "      <td>41554.0</td>\n",
       "      <td>29885.86</td>\n",
       "      <td>M1230701703</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   step      type    amount     nameOrig  oldbalanceOrg  newbalanceOrig  \\\n",
       "0     1   PAYMENT   9839.64  C1231006815       170136.0       160296.36   \n",
       "1     1   PAYMENT   1864.28  C1666544295        21249.0        19384.72   \n",
       "2     1  TRANSFER    181.00  C1305486145          181.0            0.00   \n",
       "3     1  CASH_OUT    181.00   C840083671          181.0            0.00   \n",
       "4     1   PAYMENT  11668.14  C2048537720        41554.0        29885.86   \n",
       "\n",
       "      nameDest  oldbalanceDest  newbalanceDest  isFraud  isFlaggedFraud  \n",
       "0  M1979787155             0.0             0.0        0               0  \n",
       "1  M2044282225             0.0             0.0        0               0  \n",
       "2   C553264065             0.0             0.0        1               0  \n",
       "3    C38997010         21182.0             0.0        1               0  \n",
       "4  M1230701703             0.0             0.0        0               0  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = pd.read_csv('spit.csv', sep = ',')\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bb5bb123",
   "metadata": {
    "papermill": {
     "duration": 0.01106,
     "end_time": "2023-09-16T09:20:07.484944",
     "exception": false,
     "start_time": "2023-09-16T09:20:07.473884",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Feature Explanation:\n",
    "\n",
    "- step: represents a unit of time where 1 step equals 1 hour\n",
    "- type: type of online transaction\n",
    "- amount: the amount of the transaction\n",
    "- nameOrig: customer starting the transaction\n",
    "- oldbalanceOrg: balance before the transaction\n",
    "- newbalanceOrig: balance after the transaction\n",
    "- nameDest: recipient of the transaction\n",
    "- oldbalanceDest: initial balance of recipient before the transaction\n",
    "- newbalanceDest: the new balance of recipient after the transaction\n",
    "- isFraud: fraud transaction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6d1ae7fd",
   "metadata": {
    "papermill": {
     "duration": 0.047238,
     "end_time": "2023-09-16T09:20:07.543645",
     "exception": false,
     "start_time": "2023-09-16T09:20:07.496407",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 6362620 entries, 0 to 6362619\n",
      "Data columns (total 11 columns):\n",
      " #   Column          Dtype  \n",
      "---  ------          -----  \n",
      " 0   step            int64  \n",
      " 1   type            object \n",
      " 2   amount          float64\n",
      " 3   nameOrig        object \n",
      " 4   oldbalanceOrg   float64\n",
      " 5   newbalanceOrig  float64\n",
      " 6   nameDest        object \n",
      " 7   oldbalanceDest  float64\n",
      " 8   newbalanceDest  float64\n",
      " 9   isFraud         int64  \n",
      " 10  isFlaggedFraud  int64  \n",
      "dtypes: float64(5), int64(3), object(3)\n",
      "memory usage: 534.0+ MB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7516b320",
   "metadata": {
    "papermill": {
     "duration": 2.047389,
     "end_time": "2023-09-16T09:20:09.602668",
     "exception": false,
     "start_time": "2023-09-16T09:20:07.555279",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>step</th>\n",
       "      <th>amount</th>\n",
       "      <th>oldbalanceOrg</th>\n",
       "      <th>newbalanceOrig</th>\n",
       "      <th>oldbalanceDest</th>\n",
       "      <th>newbalanceDest</th>\n",
       "      <th>isFraud</th>\n",
       "      <th>isFlaggedFraud</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>6.362620e+06</td>\n",
       "      <td>6.362620e+06</td>\n",
       "      <td>6.362620e+06</td>\n",
       "      <td>6.362620e+06</td>\n",
       "      <td>6.362620e+06</td>\n",
       "      <td>6.362620e+06</td>\n",
       "      <td>6.362620e+06</td>\n",
       "      <td>6.362620e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>2.433972e+02</td>\n",
       "      <td>1.798619e+05</td>\n",
       "      <td>8.338831e+05</td>\n",
       "      <td>8.551137e+05</td>\n",
       "      <td>1.100702e+06</td>\n",
       "      <td>1.224996e+06</td>\n",
       "      <td>1.290820e-03</td>\n",
       "      <td>2.514687e-06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.423320e+02</td>\n",
       "      <td>6.038582e+05</td>\n",
       "      <td>2.888243e+06</td>\n",
       "      <td>2.924049e+06</td>\n",
       "      <td>3.399180e+06</td>\n",
       "      <td>3.674129e+06</td>\n",
       "      <td>3.590480e-02</td>\n",
       "      <td>1.585775e-03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000e+00</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>0.000000e+00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.560000e+02</td>\n",
       "      <td>1.338957e+04</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>0.000000e+00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>2.390000e+02</td>\n",
       "      <td>7.487194e+04</td>\n",
       "      <td>1.420800e+04</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>1.327057e+05</td>\n",
       "      <td>2.146614e+05</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>0.000000e+00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>3.350000e+02</td>\n",
       "      <td>2.087215e+05</td>\n",
       "      <td>1.073152e+05</td>\n",
       "      <td>1.442584e+05</td>\n",
       "      <td>9.430367e+05</td>\n",
       "      <td>1.111909e+06</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>0.000000e+00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>7.430000e+02</td>\n",
       "      <td>9.244552e+07</td>\n",
       "      <td>5.958504e+07</td>\n",
       "      <td>4.958504e+07</td>\n",
       "      <td>3.560159e+08</td>\n",
       "      <td>3.561793e+08</td>\n",
       "      <td>1.000000e+00</td>\n",
       "      <td>1.000000e+00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               step        amount  oldbalanceOrg  newbalanceOrig  \\\n",
       "count  6.362620e+06  6.362620e+06   6.362620e+06    6.362620e+06   \n",
       "mean   2.433972e+02  1.798619e+05   8.338831e+05    8.551137e+05   \n",
       "std    1.423320e+02  6.038582e+05   2.888243e+06    2.924049e+06   \n",
       "min    1.000000e+00  0.000000e+00   0.000000e+00    0.000000e+00   \n",
       "25%    1.560000e+02  1.338957e+04   0.000000e+00    0.000000e+00   \n",
       "50%    2.390000e+02  7.487194e+04   1.420800e+04    0.000000e+00   \n",
       "75%    3.350000e+02  2.087215e+05   1.073152e+05    1.442584e+05   \n",
       "max    7.430000e+02  9.244552e+07   5.958504e+07    4.958504e+07   \n",
       "\n",
       "       oldbalanceDest  newbalanceDest       isFraud  isFlaggedFraud  \n",
       "count    6.362620e+06    6.362620e+06  6.362620e+06    6.362620e+06  \n",
       "mean     1.100702e+06    1.224996e+06  1.290820e-03    2.514687e-06  \n",
       "std      3.399180e+06    3.674129e+06  3.590480e-02    1.585775e-03  \n",
       "min      0.000000e+00    0.000000e+00  0.000000e+00    0.000000e+00  \n",
       "25%      0.000000e+00    0.000000e+00  0.000000e+00    0.000000e+00  \n",
       "50%      1.327057e+05    2.146614e+05  0.000000e+00    0.000000e+00  \n",
       "75%      9.430367e+05    1.111909e+06  0.000000e+00    0.000000e+00  \n",
       "max      3.560159e+08    3.561793e+08  1.000000e+00    1.000000e+00  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d9476149",
   "metadata": {
    "papermill": {
     "duration": 2.107751,
     "end_time": "2023-09-16T09:20:11.722658",
     "exception": false,
     "start_time": "2023-09-16T09:20:09.614907",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "step              0\n",
       "type              0\n",
       "amount            0\n",
       "nameOrig          0\n",
       "oldbalanceOrg     0\n",
       "newbalanceOrig    0\n",
       "nameDest          0\n",
       "oldbalanceDest    0\n",
       "newbalanceDest    0\n",
       "isFraud           0\n",
       "isFlaggedFraud    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b3d95f86",
   "metadata": {
    "papermill": {
     "duration": 0.012311,
     "end_time": "2023-09-16T09:20:11.747743",
     "exception": false,
     "start_time": "2023-09-16T09:20:11.735432",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "There is no null columns in dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3e849546",
   "metadata": {
    "papermill": {
     "duration": 19.605588,
     "end_time": "2023-09-16T09:20:31.366200",
     "exception": false,
     "start_time": "2023-09-16T09:20:11.760612",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>step</th>\n",
       "      <th>type</th>\n",
       "      <th>amount</th>\n",
       "      <th>nameOrig</th>\n",
       "      <th>oldbalanceOrg</th>\n",
       "      <th>newbalanceOrig</th>\n",
       "      <th>nameDest</th>\n",
       "      <th>oldbalanceDest</th>\n",
       "      <th>newbalanceDest</th>\n",
       "      <th>isFraud</th>\n",
       "      <th>isFlaggedFraud</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>PAYMENT</td>\n",
       "      <td>9839.64</td>\n",
       "      <td>C1231006815</td>\n",
       "      <td>170136.00</td>\n",
       "      <td>160296.36</td>\n",
       "      <td>M1979787155</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>PAYMENT</td>\n",
       "      <td>1864.28</td>\n",
       "      <td>C1666544295</td>\n",
       "      <td>21249.00</td>\n",
       "      <td>19384.72</td>\n",
       "      <td>M2044282225</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>TRANSFER</td>\n",
       "      <td>181.00</td>\n",
       "      <td>C1305486145</td>\n",
       "      <td>181.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C553264065</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>CASH_OUT</td>\n",
       "      <td>181.00</td>\n",
       "      <td>C840083671</td>\n",
       "      <td>181.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C38997010</td>\n",
       "      <td>21182.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>PAYMENT</td>\n",
       "      <td>11668.14</td>\n",
       "      <td>C2048537720</td>\n",
       "      <td>41554.00</td>\n",
       "      <td>29885.86</td>\n",
       "      <td>M1230701703</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6362615</th>\n",
       "      <td>743</td>\n",
       "      <td>CASH_OUT</td>\n",
       "      <td>339682.13</td>\n",
       "      <td>C786484425</td>\n",
       "      <td>339682.13</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C776919290</td>\n",
       "      <td>0.00</td>\n",
       "      <td>339682.13</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6362616</th>\n",
       "      <td>743</td>\n",
       "      <td>TRANSFER</td>\n",
       "      <td>6311409.28</td>\n",
       "      <td>C1529008245</td>\n",
       "      <td>6311409.28</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C1881841831</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6362617</th>\n",
       "      <td>743</td>\n",
       "      <td>CASH_OUT</td>\n",
       "      <td>6311409.28</td>\n",
       "      <td>C1162922333</td>\n",
       "      <td>6311409.28</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C1365125890</td>\n",
       "      <td>68488.84</td>\n",
       "      <td>6379898.11</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6362618</th>\n",
       "      <td>743</td>\n",
       "      <td>TRANSFER</td>\n",
       "      <td>850002.52</td>\n",
       "      <td>C1685995037</td>\n",
       "      <td>850002.52</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C2080388513</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6362619</th>\n",
       "      <td>743</td>\n",
       "      <td>CASH_OUT</td>\n",
       "      <td>850002.52</td>\n",
       "      <td>C1280323807</td>\n",
       "      <td>850002.52</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C873221189</td>\n",
       "      <td>6510099.11</td>\n",
       "      <td>7360101.63</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>6362620 rows × 11 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         step      type      amount     nameOrig  oldbalanceOrg  \\\n",
       "0           1   PAYMENT     9839.64  C1231006815      170136.00   \n",
       "1           1   PAYMENT     1864.28  C1666544295       21249.00   \n",
       "2           1  TRANSFER      181.00  C1305486145         181.00   \n",
       "3           1  CASH_OUT      181.00   C840083671         181.00   \n",
       "4           1   PAYMENT    11668.14  C2048537720       41554.00   \n",
       "...       ...       ...         ...          ...            ...   \n",
       "6362615   743  CASH_OUT   339682.13   C786484425      339682.13   \n",
       "6362616   743  TRANSFER  6311409.28  C1529008245     6311409.28   \n",
       "6362617   743  CASH_OUT  6311409.28  C1162922333     6311409.28   \n",
       "6362618   743  TRANSFER   850002.52  C1685995037      850002.52   \n",
       "6362619   743  CASH_OUT   850002.52  C1280323807      850002.52   \n",
       "\n",
       "         newbalanceOrig     nameDest  oldbalanceDest  newbalanceDest  isFraud  \\\n",
       "0             160296.36  M1979787155            0.00            0.00        0   \n",
       "1              19384.72  M2044282225            0.00            0.00        0   \n",
       "2                  0.00   C553264065            0.00            0.00        1   \n",
       "3                  0.00    C38997010        21182.00            0.00        1   \n",
       "4              29885.86  M1230701703            0.00            0.00        0   \n",
       "...                 ...          ...             ...             ...      ...   \n",
       "6362615            0.00   C776919290            0.00       339682.13        1   \n",
       "6362616            0.00  C1881841831            0.00            0.00        1   \n",
       "6362617            0.00  C1365125890        68488.84      6379898.11        1   \n",
       "6362618            0.00  C2080388513            0.00            0.00        1   \n",
       "6362619            0.00   C873221189      6510099.11      7360101.63        1   \n",
       "\n",
       "         isFlaggedFraud  \n",
       "0                     0  \n",
       "1                     0  \n",
       "2                     0  \n",
       "3                     0  \n",
       "4                     0  \n",
       "...                 ...  \n",
       "6362615               0  \n",
       "6362616               0  \n",
       "6362617               0  \n",
       "6362618               0  \n",
       "6362619               0  \n",
       "\n",
       "[6362620 rows x 11 columns]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.drop_duplicates()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a2eabffa",
   "metadata": {
    "papermill": {
     "duration": 1.467562,
     "end_time": "2023-09-16T09:20:32.848711",
     "exception": false,
     "start_time": "2023-09-16T09:20:31.381149",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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JIYAAIBCEkMAAEAhiSEAAKCQxBAAAFBIYggAACgkMQQAABTSZsXQ9OnT069fv3Tq1CkjR47MAw88sNG1d9xxR0aMGJGddtopO+ywQ4YNG5abb765xZqmpqZMnjw5vXv3TufOnVNVVZXHH398c0YDAADYJK2OoVmzZqWmpiZTpkzJwoULs99++2X06NFZunTpBtfvsssu+drXvpb58+fn4YcfTnV1daqrqzNnzpzmNZdddlmuvvrqXHfddbn//vuzww47ZPTo0XnllVc2/5kBAAC8iVbH0JVXXpkJEyakuro6Q4YMyXXXXZcuXbqktrZ2g+sPOeSQfPSjH80+++yTPffcM2eccUaGDh2aX//610lePys0bdq0nHvuuTn66KMzdOjQzJw5M88991zuvPPOLXpyAAAAG9OqGFqzZk0WLFiQqqqqvx+gvDxVVVWZP3/+P318U1NT6urq8qc//Snvf//7kyRPPvlk6uvrWxyze/fuGTly5EaPuXr16jQ2Nra4AQAAtEarYmj58uVZu3Ztevbs2WJ7z549U19fv9HHrVy5MjvuuGM6duyYI488Mt/85jfzoQ99KEmaH9eaY06dOjXdu3dvvvXt27c1TwMAAKBtribXtWvXPPjgg/ntb3+bb3zjG6mpqcncuXM3+3iTJk3KypUrm29PP/301hsWAAAohA6tWdyjR49UVFSkoaGhxfaGhob06tVro48rLy/PXnvtlSQZNmxYHn300UydOjWHHHJI8+MaGhrSu3fvFsccNmzYBo9XWVmZysrK1owOAADQQqvODHXs2DHDhw9PXV1d87Z169alrq4uo0aN2uTjrFu3LqtXr06S9O/fP7169WpxzMbGxtx///2tOiYAAEBrtOrMUJLU1NRk/PjxGTFiRA488MBMmzYtq1atSnV1dZLkpJNOym677ZapU6cmef3zPSNGjMiee+6Z1atX56677srNN9+ca6+9NklSVlaWM888M1//+tczcODA9O/fP+edd1769OmTsWPHbr1nCgAA8H+0OoaOP/74LFu2LJMnT059fX2GDRuW2bNnN18AYfHixSkv//sJp1WrVuX000/PM888k86dO2fw4MH57ne/m+OPP755zVlnnZVVq1blM5/5TFasWJH3ve99mT17djp16rQVniIAAMD6ypqamppKPcSWamxsTPfu3bNy5cp069at1OOs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Rn8wmD9/fq6++mq/QWWr8JkhoL2ZMmVKqUcoHDFEkmT48OEbPXsErTF27Nj1tv3pT3/KV7/61fz4xz/OJz/5yVx44YVtPxjtTmu/Z+OSSy7J5z73uey0007bZiDapbKysha/4PnH+9AW1qxZkzVr1vjC323gn387IoVQX1/f/OFQ2Fqee+65TJgwIfvuu29ee+21PPjgg7nppps2eqYStqWLL744f/3rX0s9BtuZpqam7L333tlll12yyy675MUXX8z+++/ffH/w4MGlHpF2ZsaMGfnCF76QW265JUkyadKkdO3aNd27d8+HPvShPP/88yWesH1xZogsW7Ys5513Xj7wgQ+UehTaiZUrV+biiy/ON7/5zQwbNix1dXU56KCDSj0WBed6QWyOGTNmlHoECuQb3/hGvvGNb+S9731vbr311vz617/OnXfemQsvvDDl5eW5+uqrc+655+baa68t9ajthhgqiP3333+Dp/VXrlyZZ555JoMGDcp3v/vdEkxGe3PZZZfl0ksvTa9evXLbbbf5MCiwXRs/fnypR6BAbrzxxtxwww0ZN25cfve732XkyJH5/ve/n2OOOSZJ8q53vSuf+9znSjxl++LS2gVxwQUXbHB7t27dMmjQoIwePdpltdkqysvL07lz51RVVb3pa+qOO+5ow6lg/Usiw6aora3NJz/5yVRWVpZ6FAqgsrIyTzzxRPr27dt8/+GHH86gQYOSJM8++2z69++fNWvWlHLMdsWZoYJwdRLaykknneTDxUC7MWHChBx11FHN3zPUp0+f3HvvvenXr19pB6NdevXVV1uEd8eOHfO2t72t+X6HDh18XcBWJoYK5uWXX87Pf/7z/PnPf06SDBo0KFVVVencuXOJJ6O9uPHGG0s9AsBW849voHnhhRd8PQDb1B//+MfU19cnef3199hjj+XFF19MkixfvryUo7VLYqhA/uu//iuf/vSn1/sXqUePHrnhhhvy4Q9/uESTUTRLly5t/i0rtJWDDjrIL36At7xDDz20RYQfddRRSV6/rPsbXybN1iOGCuLee+/Nsccem4985CP5t3/7t+yzzz5JXv/twxVXXJFjjz028+bNy7/+67+WeFK2d126dMlTTz3VfKn2I488Mtdff3169+6dJGloaEifPn2c5meLNTY2btK6bt26JUnuuuuubTkO7ZTvGaIt+c7HtucCCgVxxBFHpG/fvvn2t7+9wf2f/exn8/TTT/thgS1WXl6e+vr65jM///ih9YaGhvTu3dvbTNhi5eXlb/pD6Ru/QRXebIny8vJ07969+bW2YsWKdOvWLeXlLb+q0XdYwfbJmaGCuO+++3LppZdudP/nP//5Vn+bO2wuv1Vla7jnnnua/9zU1JQjjjgi119/fXbbbbcSTkV743uGaEuXXXZZvvCFLzS/pfc3v/lNRowY0XxRhRdeeCFnn312vvWtb5VyzHbFmaGC6Ny5cx577LHsscceG9z/1FNPZfDgwXn55ZfbeDLam005M+RtcmwLLp0NbO8qKiqyZMmS5r9Du3XrlgcffNDfodtQ+T9fQnswcODA3H333RvdX1dXl4EDB7bhRLRX3l8PtHevvPJKbrrppnzrW9/K448/XupxaEf+8RyFcxbbnrfJFUR1dXW+/OUvp2fPnjniiCNa7PvpT3+as846K+ecc06JpqM9aWpqyt57790cQC+++GL233//5vfX+w87sD2pqanJq6++mm9+85tJkjVr1mTUqFF55JFH0qVLl5x11ln5+c9/nlGjRpV4UmBziKGCOOOMM3LvvffmqKOOyqBBg7LPPvukqakpjz76aB5//PGMHTs2Z555ZqnHpB3w/npKyVlItraf/exnufjii5vv33LLLXnqqafy+OOPZ/fdd88pp5ySr3/96/npT39awimBzSWGCqK8vDy33357Zs2aldtuuy2PPfZYkmTw4ME5//zzc8IJJ5R4QtqL8ePHl3oECuJjH/tYi/uvvPJKPve5z2WHHXZosf2OO+5oy7FoZxYvXpwhQ4Y03//Zz36WY489tvkzuGecccZ677iALXH99ddnxx13TJK89tprufHGG9OjR48kr19Aga3LBRTYoEsuuSSf+9znstNOO5V6FIANqq6u3qR1zlayJXbaaaf89re/bf5cbf/+/XPeeefllFNOSZIsWrQo++yzjwsQsVX069dvk85w+z6irUcMsUH/ePUS2FSb+pr53//93208CcCWGzVqVI477rjU1NTkkUceydChQ/PEE0+kf//+SZJ58+Zl/PjxWbRoUWkHBTaLt8mxQRqZzbVo0aLsscce+cQnPtF8aVBoS0899VRWrVqVwYMHr/fFmNBaZ511Vk444YT89Kc/zSOPPJIjjjiiOYSS5K677sqBBx5Ywglpb9atW5cbb7wxd9xxRxYtWpSysrIMGDAgxxxzTE488USfjdzKnBlig3xfB5vr9ttvT21tbebOnZvDDz88p5xySo444gg/lLLV1dbWZsWKFampqWne9pnPfCY33HBDkmTQoEGZM2dO+vbtW6oRaSfq6uryk5/8JL169coXvvCFdOnSpXnfBRdckIMPPjiHHHJI6Qak3WhqaspRRx2V//7v/85+++2XwYMHN1/w6n/+53/ykY98JHfeeWepx2xXxBAbJIbYUs8++2xuvPHG3HjjjXnppZdy4okn5tRTT/V9Vmw1//qv/5rPfvazzZ8dmj17dj784Q/nxhtvzD777JOJEydmyJAhuf7660s8KcCmmTFjRs4444z853/+Zz7wgQ+02Hf33Xdn7Nixueaaa3LSSSeVaML2RwyxQWKIrWnevHk5//zz88tf/jLLly/PzjvvXOqRaAfe/va3Z+7cudl3332TJKeddlqWLVuWH/zgB0mSuXPnprq62geN2SKLFy/epHW77777Np6EIjjssMPywQ9+MF/96lc3uP/iiy/OvHnzMmfOnDaerP3ymSFgm3nllVfygx/8ILW1tbn//vtz3HHHtXh7CWyJl19+Od26dWu+f++99+bUU09tvj9gwIDU19eXYjTakY1d3aupqal5e1lZWV577bW2Ho126OGHH85ll1220f2HH354rr766jacqP0TQ2zQQQcdlM6dO5d6DLZT999/f2644YZ8//vfz4ABA3LKKafkhz/8oTNCbFV77LFHFixYkD322CPLly/PI488kve+973N++vr69O9e/cSTkh78Pvf/36D25uamvK9730vV199dfN3wsCW+utf/5qePXtudH/Pnj3zt7/9rQ0nav/EUEE0NjZu0ro3fst61113bctxaMfe+c53ZunSpfnEJz6RefPmZb/99iv1SLRT48ePz+c///k88sgjufvuuzN48OAMHz68ef+9996bd73rXSWckPZgQ/8N+8UvfpGvfvWr+fOf/5yzzjor//Zv/1aCyWiP1q5dmw4dNv7jeUVFhbOQW5kYKoiddtrpTS/F+Mbp/rVr17bhVLRHjz76aHbYYYfMnDkzN99880bX/fWvf23DqWiPzjrrrLz00ku544470qtXr9x+++0t9v/mN7/JCSecUKLpaI8WLlyYs88+O7/61a/y6U9/OnfddZevEGCrampqysknn5zKysoN7l+9enUbT9T+uYBCQcybN6/5z01NTTniiCNy/fXXZ7fddmux7uCDD27r0Whnbrrppk1aN378+G08Cbz+W9aKiopSj8F27i9/+UvOOeec/PCHP8zHP/7xfP3rX3eBIbaJN66O+c/MmDFjG09SHGKooFwtjm1l1apV2WGHHUo9BgX35z//OTfccENmzpyZJUuWlHoctmOnn356brjhhnzgAx/IJZdckmHDhpV6JGArEkMFJYbYVvbcc8/cdNNNed/73lfqUSiYl156KbNmzUptbW3mz5+fESNG5JhjjslXvvKVUo/Gdqy8vDydOnXK4MGD33TdwoUL22giYGvymSFgqzrmmGPywQ9+MGeccUa+8Y1vpGPHjqUeiXbuvvvuy/XXX5/bb789u+++ex599NHcc889Oeigg0o9Gu3AlClTSj0CsA05M1RQXbt2zcMPP5z+/fuXehTaofvuuy+nnHJKysvLc/PNN2f//fcv9Ui0Q1dccUVqa2uzcuXKjBs3Lp/61Key33775W1ve1seeuihDBkypNQjAvAWJ4YK4mMf+1iL+z/+8Y/zwQ9+cL3Pdtxxxx1tORbt2OrVq3PuuefmmmuuyYc+9KH1LhXqtcaW6tChQ84+++xceOGFLS6SIIZoK42Njbnllltyww035He/+12pxwE2g7fJFcQ/fvHgpz71qRJNQlGsXr06S5cuTVlZWbp37/6m35sAm+Oiiy7KjBkzcvPNN2fcuHE58cQTfa8QbeKee+5JbW1t7rjjjnTv3j0f/ehHSz0SsJmcGQK2up///Oc55ZRT0rt379x0003ZZ599Sj0S7di8efNSW1ubH/zgB9lrr73yyCOPZN68eXnve99b6tFoR5599tnceOONmTFjRlasWJG//e1vufXWW/Pxj3/8Tb/HD3hrKy/1AJTWU089lT/+8Y9Zt25dqUehnfjsZz+bD3/4w5kwYULmz58vhNjmDj744Nx0002pr6/P6aefnuHDh+fggw/Oe97znlx55ZWlHo/t3A9/+MMcccQRGTRoUB588MFcccUVee6551JeXp59991XCMF2TgwVRG1t7Xo/FHzmM5/JgAEDsu++++Zd73pXnn766RJNR3vym9/8Jvfee28mT5683pddNjU15b//+79z7LHHlmg62rOuXbvms5/9bO6///48+OCDGTlyZC655JJSj8V27vjjj8/++++fJUuW5Pbbb8/RRx/tKpnQjoihgviP//iP7Lzzzs33Z8+enRkzZmTmzJn57W9/m5122ikXXHBBCSekvVi4cGEOOOCAFtuefPLJnHfeedl9993z0Y9+NK+88kqJpqM9ufvuuzNkyJA0Njaut69v376ZM2dObr311hJMRnty6qmnZvr06RkzZkyuu+66/O1vfyv1SMBWJIYK4vHHH8+IESOa7//nf/5njj766Hzyk5/MAQcckIsvvjh1dXUlnJD24o3fmK5evTq33HJLPvjBD2bQoEG5+OKLU1NTk6VLl+YnP/lJiaekPZg2bVomTJiQbt26rbeve/fu+dznPpfp06eXYDLak29/+9tZsmRJPvOZz+S2225L7969c/TRR6epqclbzKEdEEMF8fLLL7f4geHee+/N+9///ub7AwYMSH19fSlGo51ZsGBBTj/99PTq1SvTpk3L2LFj8/TTT6e8vDyjR4/e4A+usDkeeuihjBkzZqP7DzvssCxYsKANJ6K96ty5c8aPH5958+blf/7nf/LOd74zPXv2zHvf+9584hOf8FUBsB0TQwWxxx57NP9QsHz58jzyyCMtrrRUX1+/3uW3YXOMHDkylZWVue+++/Lb3/42X/ziF9OzZ89Sj0U71NDQkLe97W0b3d+hQ4csW7asDSeiCAYOHJiLL744Tz/9dL773e/mpZdeyrhx40o9FrCZfPFHQYwfPz6f//zn88gjj+Tuu+/O4MGDM3z48Ob99957r+/nYKs49NBDc8MNN2Tp0qU58cQTM3r0aFdbYpvYbbfd8oc//CF77bXXBvc//PDD6d27dxtPRVGUl5fnwx/+cKqqqnLNNdeUehxgMzkzVBBnnXVWJkyYkDvuuCOdOnXK7bff3mL/b37zm5xwwgklmo72ZM6cOXnkkUey995757TTTkvv3r1zxhlnJIkoYqs64ogjct55523wghwvv/xypkyZkqOOOqoEk9HeLFu2LD/5yU/ys5/9LGvXrk2SvPrqq7nqqqsyYMCAXHrppSWeENhcvnSVZmvXrl3vUsiwpX7xi1+ktrY2P/rRj9K3b98ce+yxOfbYY9e74hy0VkNDQw444IBUVFRk4sSJGTRoUJLksccey/Tp07N27dosXLjQ2zTZIr/+9a9z1FFHpbGxMWVlZRkxYkRmzJiRsWPHpkOHDvniF7+Y8ePHp3PnzqUeFdgMYoj8+c9/zg033JCZM2dmyZIlpR6H7dzatWtz+eWX57/+67+yZs2aHHrooZkyZUpeeeWVfPe7301tbW0efvjh5t+uwpZ46qmnctppp2XOnDl546+zsrKyjB49OtOnT0///v1LPCHbu0MOOSR9+vTJOeeck5tuuilXXHFFBg4cmG984xu+Mw3aATFUUC+99FJmzZqV2trazJ8/PyNGjMgxxxyTr3zlK6Ueje3cRRddlPPPPz9VVVXp3Llz5syZk3HjxqW2trZ5zYa+iwi2xN/+9rc88cQTaWpqysCBA1t8rxpsibe//e351a9+lSFDhuTll1/OjjvumDvuuCNHH310qUcDtgIxVDD33Xdfrr/++tx+++3Zfffd8+ijj+aee+7JQQcdVOrRaCcGDhyYL3/5y/nsZz+b5PW3yR155JF5+eWXU17uY4rA9qW8vDz19fXZddddkyRdu3bNgw8+mD333LPEkwFbg6vJFcQVV1yR2trarFy5MuPGjcsvf/nL7Lfffnnb296Wt7/97aUej3Zk8eLFOeKII5rvV1VVpaysLM8991z+5V/+pYSTAWyeP/7xj83fxdfU1JQ//elPWbVqVYs1Q4cOLcVowBZyZqggOnTokLPPPjsXXnhhi4skvO1tb8tDDz2UIUOGlHA62pOKiorU19fnHe94R/O2rl275uGHH/b5DWC7U15enrKysmzox6U3tpeVlfkcJGynnBkqiIsuuigzZszIzTffnHHjxuXEE0/0vUJsE01NTTn55JNTWVnZvO2VV17J5z73ueywww7N23xjO7A9ePLJJ0s9ArANOTNUMPPmzUttbW1+8IMfZK+99sojjzySefPm5b3vfW+pR6OdqK6u3qR1M2bM2MaTAGy5Cy+8MF/+8pfTpUuXUo8CbANiqKBeeOGF3Hrrramtrc2CBQty4IEH5thjj01NTU2pRwOAt4yKioosWbKk+QIKQPsihsgf/vCH3HDDDbnllluydOnSUo8DAG8Z/3g1OaB9cZ3bgrj77rszZMiQNDY2rrevb9++mTNnTm699dYSTAYAb21lZWWlHgHYRpwZKoiPfOQj+cAHPpAvfelLG9x/9dVX55577smPfvSjNp4MAN66ysvL0717938aRH/961/baCJga3I1uYJ46KGHcumll250/2GHHZbLL7+8DScCgO3DBRdckO7du5d6DGAbEEMF0dDQkLe97W0b3d+hQ4csW7asDScCgO3DCSec4DND0E75zFBB7LbbbvnDH/6w0f0PP/xwevfu3YYTAcBbn88LQfsmhgriiCOOyHnnnZdXXnllvX0vv/xypkyZkqOOOqoEkwHAW5ePVkP75gIKBdHQ0JADDjggFRUVmThxYgYNGpQkeeyxxzJ9+vSsXbs2CxcuTM+ePUs8KQAAtA0xVCBPPfVUTjvttMyZM6f5N11lZWUZPXp0pk+fnv79+5d4QgAAaDtiqID+9re/5YknnkhTU1MGDhyYnXfeudQjAQBAmxNDAABAIbmAAgAAUEhiCAAAKCQxBAAAFJIYAgAACkkMAfCWdMghh+TMM88s9RgAtGNiCAAAKCQxBMBbzsknn5x58+blqquuSllZWcrKytKhQ4dcfvnlLdY9+OCDKSsryxNPPJHk9S+Svvbaa3P44Yenc+fOGTBgQH7wgx+0eMzTTz+dj3/849lpp52yyy675Oijj86iRYva6qkB8BYihgB4y7nqqqsyatSoTJgwIUuWLMmSJUtywQUXZMaMGS3WzZgxI+9///uz1157NW8777zzcswxx+Shhx7KJz/5yZxwwgl59NFHkySvvvpqRo8ena5du+ZXv/pVfvOb32THHXfMmDFjsmbNmjZ9jgCUnhgC4C2ne/fu6dixY7p06ZJevXqlV69eqa6uzp/+9Kc88MADSV4Pm1tvvTWnnHJKi8ced9xx+fSnP5299947F110UUaMGJFvfvObSZJZs2Zl3bp1uf7667Pvvvtmn332yYwZM7J48eLMnTu3rZ8mACUmhgDYLvTp0ydHHnlkamtrkyQ//vGPs3r16hx33HEt1o0aNWq9+2+cGXrooYfyxBNPpGvXrtlxxx2z4447Zpdddskrr7ySv/zlL23zRAB4y+hQ6gEAYFN9+tOfzoknnpj/9//+X2bMmJHjjz8+Xbp02eTHv/jiixk+fHhuueWW9fa94x3v2JqjArAdEEMAvCV17Ngxa9eubbHtiCOOyA477JBrr702s2fPzi9/+cv1HnffffflpJNOanF///33T5IccMABmTVrVnbdddd069Zt2z4BAN7yvE0OgLekfv365f7778+iRYuyfPnyrFu3LhUVFTn55JMzadKkDBw4cL23xCXJ7bffntra2vz5z3/OlClT8sADD2TixIlJkk9+8pPp0aNHjj766PzqV7/Kk08+mblz5+aLX/xinnnmmbZ+igCUmBgC4C3py1/+cioqKjJkyJC84x3vyOLFi5Mkp556atasWZPq6uoNPu6CCy7I9773vQwdOjQzZ87MbbfdliFDhiRJunTpkl/+8pfZfffd87GPfSz77LNPTj311LzyyivOFAEUUFlTU1NTqYcAgE31q1/9Koceemiefvrp9OzZs8W+srKy/OhHP8rYsWNLMxwA2xWfGQJgu7B69eosW7Ys559/fo477rj1QggAWsvb5ADYLtx2223ZY489smLFilx22WWlHgeAdsDb5AAAgEJyZggAACgkMQQAABSSGAIAAApJDAEAAIUkhgAAgEISQwAAQCGJIQAAoJDEEAAAUEhiCAAAKKT/D8DfPKYaYchEAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1000x700 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = plt.figure(figsize =(10, 7))\n",
    "data['type'].value_counts(normalize=True).plot(kind='bar')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8850fc85",
   "metadata": {
    "papermill": {
     "duration": 0.154688,
     "end_time": "2023-09-16T09:20:33.016776",
     "exception": false,
     "start_time": "2023-09-16T09:20:32.862088",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No Frauds Percentage: 99.87091795518198\n",
      "Frauds Percentage: 0.12908204481801522\n"
     ]
    }
   ],
   "source": [
    "print(\"No Frauds Percentage:\",data['isFraud'].value_counts()[0]/len(data['isFraud'])*100)\n",
    "print(\"Frauds Percentage:\",data['isFraud'].value_counts()[1]/len(data['isFraud'])*100)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "742d65af",
   "metadata": {
    "papermill": {
     "duration": 0.013209,
     "end_time": "2023-09-16T09:20:33.043161",
     "exception": false,
     "start_time": "2023-09-16T09:20:33.029952",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Imbalance dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "4b6ce143",
   "metadata": {
    "papermill": {
     "duration": 0.217537,
     "end_time": "2023-09-16T09:20:33.274019",
     "exception": false,
     "start_time": "2023-09-16T09:20:33.056482",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "data.drop(['isFlaggedFraud','nameOrig','nameDest'], axis = 1, inplace = True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5305a856",
   "metadata": {
    "papermill": {
     "duration": 2.134414,
     "end_time": "2023-09-16T09:20:35.422240",
     "exception": false,
     "start_time": "2023-09-16T09:20:33.287826",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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7d69WyaTSTt27FBycrIkadWqVapfv77hfH369FHv3r21Y8cORUZGqlmzZjp//rykWwOcIkWK6Msvv9TevXs1ZMgQvfXWW1q4cGGm9V+9elXR0dHaunWr4uPj5eLiopYtW8psNhv6DRw4UDExMdq5c6dKlSqltm3b6ubNm5KknTt3qlGjRipbtqw2bNigtWvXqlmzZkpLS5MkxcbGat68eZo6dap++eUX9erVSy+++KJ10PjFF1/I29tbr732Wrr6evfurdTUVH311VfWtmvXrum9997Txx9/rF9++UUFCxZM97ro6GitW7dO3377rVasWKE1a9Zo+/btmX8jAQAAABszW0zZ9sgJ7ms7+YoVK2ro0KGSpPDwcE2aNEnx8fHy9PTU5s2bdebMGbm7u0uSxo4dqyVLlmjRokX6z3/+owYNGighIUExMTFKSEjQ448/rv3792vt2rVq0qSJEhIS1LdvX8P5unXrpmeffVaS9NFHHykuLk4zZ85U37595erqquHDh1v7Fi9eXBs2bNDChQvVunXrDOu/fazbZs2apQIFCmjv3r0qX768tT0mJkZPPfWUJGn48OEqV66cDh06pDJlymj06NGqXr26pkyZYu1frlw5SVJKSopGjhypn376SZGRkZKksLAwrV27VtOmTVP9+vX166+/qkSJEnJzc0tXX6FCheTr66tff/3V2paamqopU6aoUqVKGb6nK1euaO7cufr888/VqFEjSdLs2bNVqFChDPvflpKSopSUFEObxWKRyZQz/kMGAAAAHmT3lXhVrFjR8HVwcLDOnDmjxMREJScnK3/+/PL29rY+jh49ap3KV79+fa1du1ZpaWlatWqVGjRoYB2MnThxQocOHVKDBg0Mx789eJGk3Llzq3r16tq3b5+1bfLkyapWrZoKFCggb29vTZ8+XUlJSZnWf/DgQbVt21ZhYWHy9fVVaGioJKV7zd/fZ3BwsCTpzJkzkv6XeGXk0KFDunbtmh5//HHDdZg3b55hSqMlCxNT3dzc0l33vzty5IhSU1NVo0YNa5ufn59Kly59x+PGxsbKz8/P8LCYr9x1XQAAAMDfsauh0X0lXq6uroavTSaTzGazkpOTFRwcbJ1K+He3N4GoV6+erly5ou3bt2v16tUaOXKkgoKCNGrUKFWqVEmFChVSeHj4Xdcyf/58xcTEaNy4cYqMjJSP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wg3sAAAAkI0sFku2PXICBl73YevWrerevbtGjBihAwcOKC4uTvXq1bvr18+dO1dubm5at26dpk6dKklycXHRBx98oF9++UVz587Vzz//rL59+2aprnHjxmnOnDmaNWuW1q5dqwsXLujrr7/O0jEAAAAA2A5TDe9DUlKS8uTJo6efflo+Pj4qVqyYqlSpYujz/fffy9vb2/p106ZN9eWXX0qSwsPDNXr0aEP/v2/aERoaqnfeeUevv/66pkyZctd1TZgwQQMGDFCrVq0kSVOnTtXy5cvv+JqUlBSlpKQY2iwWi0wm012fFwAAALiNNV5GDLzuw+OPP65ixYopLCxMTZo0UZMmTdSyZUt5eXlZ+zRs2FAfffSR9es8efJY/12tWrV0x/zpp58UGxur/fv36/Lly7p586auX7+ua9euGY6bmUuXLunkyZOqWbOmtS137tyqXr36HWPY2NhYDR8+3NDm7ppXnm53v54NAAAAQMaYangffHx8tH37dn3xxRcKDg7WkCFDVKlSJV28eNHaJ0+ePCpZsqT1ERwcbHju744dO6ann35aFStW1FdffaVt27Zp8uTJkm5tviHdmor4zwFUamrqfb+XAQMG6NKlS4aHh2ve+z4uAAAAHk6s8TJi4HWfcufOrcaNG2v06NHatWuXjh07pp9//vmejrVt2zaZzWaNGzdOtWrVUqlSpXTixAlDnwIFCujUqVOG/8B27txp/befn5+Cg4O1adMma9vNmze1bdu2O57b3d1dvr6+hgfTDAEAAADbYKrhffj+++915MgR1atXT3nz5tWyZctkNptVunTpezpeyZIllZqaqg8//FDNmjUzbLpxW4MGDXT27FmNHj1azz33nOLi4vTDDz/I19fX2qdHjx4aNWqUwsPDVaZMGY0fP96QwgEAAAD2Zs4hSVR2IfG6D/7+/lq8eLEee+wxRUREaOrUqfriiy9Urly5ezpepUqVNH78eL333nsqX768PvvsM8XGxhr6REREaMqUKZo8ebIqVaqkzZs3KyYmxtCnd+/e6tChgzp16qTIyEj5+PioZcuW9/w+AQAAANwfkyWnTIpEtsvrXdLRJTi9vB4+ji7BqZ28esHRJTi91LSbji7BqTHh2/6YVm9/V/9Y7egSnJprQJijS8hUkH9Etp3r1MV92Xaue0XiBQAAAAB2xhovAAAAADbHxDojEi8AAAAAsDMSLwAAAAA2ZxaJ19+ReAEAAACAnTHwAgAAAAA7Y6ohAAAAAJtjcw0jEi8AAAAAsDMSLwAAAAA2ZybxMiDxAgAAAAA7I/ECAAAAYHOs8TIi8QIAAAAAOyPxAgAAAGBz3EDZiMQLAAAAAOyMxAsAAACAzbHGy4jECwAAAADsjMQLAAAAgM1xHy8jEi8AAAAAsDMSLwAAAAA2Z2FXQwMSLwAAAACwMxIvAAAAADbHGi8jEi8AAAAAsDMSLwAAAAA2x328jEi8AAAAAMDOGHgBAAAAsDlLNv4vqyZPnqzQ0FB5eHioZs2a2rx58x37f/nllypTpow8PDxUoUIFLVu2LMvnZOAFAAAA4KGxYMECRUdHa+jQodq+fbsqVaqkqKgonTlzJsP+69evV9u2bdW5c2ft2LFDLVq0UIsWLbRnz54snddkYfIlMpHXu6SjS3B6eT18HF2CUzt59YKjS3B6qWk3HV2CUzM5uoCHgMnEVba3q3+sdnQJTs01IMzRJWTK3aNotp3r8qVDSklJMZ7f3V3u7u7p+tasWVOPPPKIJk2aJEkym80qWrSo3nzzTfXv3z9d/zZt2ujq1av6/vvvrW21atVS5cqVNXXq1LuukcQLAAAAgM1ZLJZse8TGxsrPz8/wiI2NTVfTjRs3tG3bNjVu3Nja5uLiosaNG2vDhg0Zvo8NGzYY+ktSVFRUpv0zw66GAAAAAHK0AQMGKDo62tCWUdp17tw5paWlKTAw0NAeGBio/fv3Z3jsU6dOZdj/1KlTWaqRgRcAAAAAm8vOFU2ZTSt8kDDVEAAAAMBDISAgQLly5dLp06cN7adPn1ZQUFCGrwkKCspS/8ww8AIAAABgc5ZsfNwtNzc3VatWTfHx8dY2s9ms+Ph4RUZGZviayMhIQ39JWrFiRab9M8NUQwAAAAAPjejoaHXq1EnVq1dXjRo1NGHCBF29elUvv/yyJKljx44qXLiwdXOOHj16qH79+ho3bpyeeuopzZ8/X1u3btX06dOzdmIL4ASuX79uGTp0qOX69euOLsVpcY3tj2tsX1xf++Ma2xfX1/64xg+PDz/80BISEmJxc3Oz1KhRw7Jx40brc/Xr17d06tTJ0H/hwoWWUqVKWdzc3CzlypWzLF26NMvn5D5ecAqXL1+Wn5+fLl26JF9fX0eX45S4xvbHNbYvrq/9cY3ti+trf1xj2BNrvAAAAADAzhh4AQAAAICdMfACAAAAADtj4AWn4O7urqFDhz7wN87LybjG9sc1ti+ur/1xje2L62t/XGPYE5trAAAAAICdkXgBAAAAgJ0x8AIAAAAAO2PgBQAAAAB2xsALAAAAAOyMgRcAAAAA2BkDLziF3377Tb/99pujy3A6q1ev1s2bN9O137x5U6tXr3ZARQAeJK+88oquXLmSrv3q1at65ZVXHFARADy42E4eOdbNmzc1fPhwffDBB0pOTpYkeXt7680339TQoUPl6urq4Apzvly5cunkyZMqWLCgof38+fMqWLCg0tLSHFSZc7h8+XKG7SaTSe7u7nJzc8vmioCsyewz4ty5cwoKCsrwDzcA8LDK7egCgHv15ptvavHixRo9erQiIyMlSRs2bNCwYcN0/vx5ffTRRw6uMOezWCwymUzp2s+fP688efI4oCLn4u/vn+H1va1IkSJ66aWXNHToULm4MEHhXkRHR2fYbjKZ5OHhoZIlS6p58+bKly9fNleWs12+fFkWi0UWi0VXrlyRh4eH9bm0tDQtW7Ys3WAM94Y/gNlHq1at7rrv4sWL7VgJHiYMvJBjff7555o/f76aNm1qbatYsaKKFi2qtm3bMvC6D7d/IJlMJr300ktyd3e3PpeWlqZdu3apdu3ajirPacyZM0cDBw7USy+9pBo1akiSNm/erLlz52rQoEE6e/asxo4dK3d3d7311lsOrjZn2rFjh7Zv3660tDSVLl1akvTrr78qV65cKlOmjKZMmaLevXtr7dq1Klu2rIOrzTlu/9HAZDKpVKlS6Z43mUwaPny4AypzPplNTEpJSSEVvw9+fn7Wf1ssFn399dfy8/NT9erVJUnbtm3TxYsXszRAA/4NAy/kWO7u7goNDU3XXrx4cX4Y3afbP5AsFot8fHzk6elpfc7NzU21atVSly5dHFWe05g7d67GjRun1q1bW9uaNWumChUqaNq0aYqPj1dISIjeffddBl736HaaNXv2bPn6+kqSLl26pFdffVV169ZVly5d1K5dO/Xq1UvLly93cLU5x8qVK2WxWPTYY4/pq6++MiSGbm5uKlasmAoVKuTACnO+Dz74QNKtQezHH38sb29v63NpaWlavXq1ypQp46jycrzZs2db/92vXz+1bt1aU6dOVa5cuSTdusZdu3a1fm4AtsAaL+RYI0aM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vlq5cqU++ugjdejQQZMnT9Yff/yhadOmadSoUY4uD06ENV7Isfr27athw4bJy8tL0q1d4pYsWaKIiAhFRUU5uDrnsGrVKsPXtxcclyxZUrlz83ebe9WzZ0/9/PPPio+PV4ECBQzPnTlzRo8//rgaNmzIDazvw9KlS9W8eXP17NlTvXv3VnBwsCTp5MmTGjNmjD788EN98803evLJJx1cac519epVvffee1q8eLGOHTsmk8mk4sWL67nnnlNMTIz1sxl40IWEhGjevHlq0KCBfH19tX37dpUsWVKffPKJvvjiCy1btszRJcJJMPBCjvX444/r2Wef1euvv66LFy+qTJkycnV11blz5zR+/Hj997//dXSJQIb+/PNP1axZU6dOndKLL76oMmXKyGKxaN++ffr8888VFBSkjRs3cv+Y+9CgQQPVrVtX77zzTobPDxo0SGvXrmWDmHt048YN1a5dW3v27FHTpk0N/w3HxcWpatWqWr16tVxdXR1dao5nsVi0bds26+A2LCxMlStXvuOtPpA13t7e2rt3r0JCQlSkSBEtXrxYNWrU0NGjR1WhQgU2MIHN8Cdr5Fg7duywJgKLFi1SYGCgduzYoa+++kpDhgxh4GUjhw8f1oQJE7Rv3z5JtxZ69+jRQyVKlHBwZTlX3rx5tWnTJr311luaP3++9cbJ/v7+ateunUaOHMmg6z5t375d06ZNy/T5Dh066IMPPsjGipzLRx99pN9//12JiYkqXbq04bn9+/erQYMGmjp1qt58800HVegcVq5cqc6dO+v48eOG+/0VL15cs2bN4rYpNhIWFqajR48qJCREZcqU0cKFC1WjRg1999138vf3d3R5cCIuji4AuFfXrl2Tj4+PJOnHH39Uq1at5OLiolq1aun48eMOrs45LF++XGXLltXmzZtVsWJFVaxYUZs2bVK5cuW0YsUKR5eXo+XNm1cfffSRzp8/r1OnTunUqVM6f/68pk6dyqDLBtLS0u6Ytri6urJg/j4sXrxYgwcPTjfokqQyZcpo4MCBWrRokQMqcx6HDh3S008/rdDQUC1evFj79u3T3r179eWXX6pIkSJ68skndeTIEUeX6RRefvllJSYmSpL69++vyZMny8PDQ7169VKfPn0cXB2cCVMNkWNVrFhRr776qlq2bKny5csrLi5OkZGR2rZtm5566imdOnXK0SXm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",
      "text/plain": [
       "<Figure size 1000x700 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "correlationdata = data.copy()\n",
    "correlationdata.drop(['type'], axis = 1, inplace = True)\n",
    "\n",
    "fig = plt.figure(figsize =(10, 7))\n",
    "sns.heatmap(correlationdata.corr(), annot = True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a38c13b",
   "metadata": {
    "papermill": {
     "duration": 0.014417,
     "end_time": "2023-09-16T09:20:35.451548",
     "exception": false,
     "start_time": "2023-09-16T09:20:35.437131",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "There is no correlation between columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "0913c9dd",
   "metadata": {
    "papermill": {
     "duration": 1.411367,
     "end_time": "2023-09-16T09:20:36.877337",
     "exception": false,
     "start_time": "2023-09-16T09:20:35.465970",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>step</th>\n",
       "      <th>amount</th>\n",
       "      <th>oldbalanceOrg</th>\n",
       "      <th>newbalanceOrig</th>\n",
       "      <th>oldbalanceDest</th>\n",
       "      <th>newbalanceDest</th>\n",
       "      <th>isFraud</th>\n",
       "      <th>type_CASH_OUT</th>\n",
       "      <th>type_DEBIT</th>\n",
       "      <th>type_PAYMENT</th>\n",
       "      <th>type_TRANSFER</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>9839.64</td>\n",
       "      <td>170136.0</td>\n",
       "      <td>160296.36</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>1864.28</td>\n",
       "      <td>21249.0</td>\n",
       "      <td>19384.72</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>181.00</td>\n",
       "      <td>181.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>181.00</td>\n",
       "      <td>181.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>21182.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>11668.14</td>\n",
       "      <td>41554.0</td>\n",
       "      <td>29885.86</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   step    amount  oldbalanceOrg  newbalanceOrig  oldbalanceDest  \\\n",
       "0     1   9839.64       170136.0       160296.36             0.0   \n",
       "1     1   1864.28        21249.0        19384.72             0.0   \n",
       "2     1    181.00          181.0            0.00             0.0   \n",
       "3     1    181.00          181.0            0.00         21182.0   \n",
       "4     1  11668.14        41554.0        29885.86             0.0   \n",
       "\n",
       "   newbalanceDest  isFraud  type_CASH_OUT  type_DEBIT  type_PAYMENT  \\\n",
       "0             0.0        0          False       False          True   \n",
       "1             0.0        0          False       False          True   \n",
       "2             0.0        1          False       False         False   \n",
       "3             0.0        1           True       False         False   \n",
       "4             0.0        0          False       False          True   \n",
       "\n",
       "   type_TRANSFER  \n",
       "0          False  \n",
       "1          False  \n",
       "2           True  \n",
       "3          False  \n",
       "4          False  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataf = pd.get_dummies(data = data,columns = ['type'], drop_first = True)\n",
    "dataf.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "85effc3d",
   "metadata": {
    "papermill": {
     "duration": 8.31277,
     "end_time": "2023-09-16T09:20:45.204551",
     "exception": false,
     "start_time": "2023-09-16T09:20:36.891781",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>step</th>\n",
       "      <th>amount</th>\n",
       "      <th>oldbalanceOrg</th>\n",
       "      <th>newbalanceOrig</th>\n",
       "      <th>oldbalanceDest</th>\n",
       "      <th>newbalanceDest</th>\n",
       "      <th>isFraud</th>\n",
       "      <th>type_CASH_OUT</th>\n",
       "      <th>type_DEBIT</th>\n",
       "      <th>type_PAYMENT</th>\n",
       "      <th>type_TRANSFER</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>-1.329609</td>\n",
       "      <td>-0.332932</td>\n",
       "      <td>1.452991</td>\n",
       "      <td>1.111175</td>\n",
       "      <td>-0.140722</td>\n",
       "      <td>-0.193057</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>-1.329609</td>\n",
       "      <td>-0.373762</td>\n",
       "      <td>0.065610</td>\n",
       "      <td>0.134375</td>\n",
       "      <td>-0.140722</td>\n",
       "      <td>-0.193057</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>-1.329609</td>\n",
       "      <td>-0.382380</td>\n",
       "      <td>-0.130708</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>-0.140722</td>\n",
       "      <td>-0.193057</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>-1.329609</td>\n",
       "      <td>-0.382380</td>\n",
       "      <td>-0.130708</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>-0.118260</td>\n",
       "      <td>-0.193057</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>-1.329609</td>\n",
       "      <td>-0.323571</td>\n",
       "      <td>0.254820</td>\n",
       "      <td>0.207169</td>\n",
       "      <td>-0.140722</td>\n",
       "      <td>-0.193057</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       step    amount  oldbalanceOrg  newbalanceOrig  oldbalanceDest  \\\n",
       "0 -1.329609 -0.332932       1.452991        1.111175       -0.140722   \n",
       "1 -1.329609 -0.373762       0.065610        0.134375       -0.140722   \n",
       "2 -1.329609 -0.382380      -0.130708        0.000000       -0.140722   \n",
       "3 -1.329609 -0.382380      -0.130708        0.000000       -0.118260   \n",
       "4 -1.329609 -0.323571       0.254820        0.207169       -0.140722   \n",
       "\n",
       "   newbalanceDest  isFraud  type_CASH_OUT  type_DEBIT  type_PAYMENT  \\\n",
       "0       -0.193057      0.0            0.0         0.0           1.0   \n",
       "1       -0.193057      0.0            0.0         0.0           1.0   \n",
       "2       -0.193057      1.0            0.0         0.0           0.0   \n",
       "3       -0.193057      1.0            1.0         0.0           0.0   \n",
       "4       -0.193057      0.0            0.0         0.0           1.0   \n",
       "\n",
       "   type_TRANSFER  \n",
       "0            0.0  \n",
       "1            0.0  \n",
       "2            1.0  \n",
       "3            0.0  \n",
       "4            0.0  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.preprocessing import RobustScaler\n",
    "rscaler = RobustScaler()\n",
    "scaled_data = rscaler.fit_transform(dataf)\n",
    "data_sc = pd.DataFrame(scaled_data, columns = dataf.columns)\n",
    "\n",
    "data_sc.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "05330962",
   "metadata": {
    "papermill": {
     "duration": 0.014714,
     "end_time": "2023-09-16T09:20:45.234720",
     "exception": false,
     "start_time": "2023-09-16T09:20:45.220006",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Model Training"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "ab04ab45",
   "metadata": {
    "papermill": {
     "duration": 0.677103,
     "end_time": "2023-09-16T09:20:45.926919",
     "exception": false,
     "start_time": "2023-09-16T09:20:45.249816",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "nonfraud = dataf[dataf['isFraud']==0]\n",
    "fraud = dataf[dataf['isFraud']==1]\n",
    "nonfraud = nonfraud.sample(n=8300, random_state = 1)\n",
    "\n",
    "frauddata = pd.merge(fraud,nonfraud, how = \"outer\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "81a72769",
   "metadata": {
    "papermill": {
     "duration": 0.026357,
     "end_time": "2023-09-16T09:20:45.968282",
     "exception": false,
     "start_time": "2023-09-16T09:20:45.941925",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "x = frauddata.drop('isFraud', axis = 1)\n",
    "y = frauddata['isFraud']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "acdf8d70",
   "metadata": {
    "papermill": {
     "duration": 0.163432,
     "end_time": "2023-09-16T09:20:46.147573",
     "exception": false,
     "start_time": "2023-09-16T09:20:45.984141",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "\n",
    "x_train,x_test,y_train,y_test = train_test_split(x,y,train_size = 0.3, random_state = 42)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a9233287",
   "metadata": {
    "papermill": {
     "duration": 0.014458,
     "end_time": "2023-09-16T09:20:46.176991",
     "exception": false,
     "start_time": "2023-09-16T09:20:46.162533",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "#### Logistic Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "7148d25e",
   "metadata": {
    "papermill": {
     "duration": 0.258178,
     "end_time": "2023-09-16T09:20:46.516120",
     "exception": false,
     "start_time": "2023-09-16T09:20:46.257942",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#LogisticRegression\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "logreg = LogisticRegression()\n",
    "logreg.fit(x_train,y_train)\n",
    "\n",
    "y_pred = logreg.predict(x_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "de94f1f2",
   "metadata": {
    "papermill": {
     "duration": 0.031956,
     "end_time": "2023-09-16T09:20:46.581348",
     "exception": false,
     "start_time": "2023-09-16T09:20:46.549392",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "#### Decision Tree Classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "5646fe02",
   "metadata": {
    "papermill": {
     "duration": 0.250591,
     "end_time": "2023-09-16T09:20:46.865232",
     "exception": false,
     "start_time": "2023-09-16T09:20:46.614641",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#DecisionTreeClassifier\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "\n",
    "dt = DecisionTreeClassifier()\n",
    "dt.fit(x_train,y_train)\n",
    "\n",
    "y_pred_dt = dt.predict(x_test)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5e60d525",
   "metadata": {
    "papermill": {
     "duration": 0.016293,
     "end_time": "2023-09-16T09:20:46.897335",
     "exception": false,
     "start_time": "2023-09-16T09:20:46.881042",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "#### Random Forest Classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "6d5a5257",
   "metadata": {
    "papermill": {
     "duration": 0.943653,
     "end_time": "2023-09-16T09:20:47.856577",
     "exception": false,
     "start_time": "2023-09-16T09:20:46.912924",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#RandomForestClassifier\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "\n",
    "rf = RandomForestClassifier()\n",
    "rf.fit(x_train,y_train)\n",
    "\n",
    "y_pred_rf = rf.predict(x_test)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f31ed94b",
   "metadata": {
    "papermill": {
     "duration": 0.015521,
     "end_time": "2023-09-16T09:20:47.887898",
     "exception": false,
     "start_time": "2023-09-16T09:20:47.872377",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "#### Gradient Boosting\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "13152d08",
   "metadata": {
    "papermill": {
     "duration": 1.024676,
     "end_time": "2023-09-16T09:20:48.927788",
     "exception": false,
     "start_time": "2023-09-16T09:20:47.903112",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#GradientBoosting\n",
    "from sklearn.ensemble import GradientBoostingClassifier\n",
    "\n",
    "gb = GradientBoostingClassifier()\n",
    "gb.fit(x_train,y_train)\n",
    "\n",
    "y_pred_gb = gb.predict(x_test)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5d3e9db3",
   "metadata": {
    "papermill": {
     "duration": 0.015052,
     "end_time": "2023-09-16T09:20:48.958457",
     "exception": false,
     "start_time": "2023-09-16T09:20:48.943405",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "#### Classification Reports and Evaluations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "687aca80",
   "metadata": {
    "papermill": {
     "duration": 0.052797,
     "end_time": "2023-09-16T09:20:49.026751",
     "exception": false,
     "start_time": "2023-09-16T09:20:48.973954",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Logistic Regression classification report: \n",
      "\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "           0       0.90      0.90      0.90      5779\n",
      "           1       0.90      0.90      0.90      5781\n",
      "\n",
      "    accuracy                           0.90     11560\n",
      "   macro avg       0.90      0.90      0.90     11560\n",
      "weighted avg       0.90      0.90      0.90     11560\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import accuracy_score, classification_report\n",
    "print(\"Logistic Regression classification report: \\n\\n\"  ,classification_report(y_test,y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "fe6748ce",
   "metadata": {
    "papermill": {
     "duration": 0.054334,
     "end_time": "2023-09-16T09:20:49.096369",
     "exception": false,
     "start_time": "2023-09-16T09:20:49.042035",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Decision Tree classification report: \n",
      "\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "           0       0.99      0.98      0.99      5779\n",
      "           1       0.98      0.99      0.99      5781\n",
      "\n",
      "    accuracy                           0.99     11560\n",
      "   macro avg       0.99      0.99      0.99     11560\n",
      "weighted avg       0.99      0.99      0.99     11560\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(\"Decision Tree classification report: \\n\\n\"  ,classification_report(y_test,y_pred_dt))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "f90676c3",
   "metadata": {
    "papermill": {
     "duration": 0.054906,
     "end_time": "2023-09-16T09:20:49.166710",
     "exception": false,
     "start_time": "2023-09-16T09:20:49.111804",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Random Forest classification report: \n",
      "\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "           0       1.00      0.99      0.99      5779\n",
      "           1       0.99      1.00      0.99      5781\n",
      "\n",
      "    accuracy                           0.99     11560\n",
      "   macro avg       0.99      0.99      0.99     11560\n",
      "weighted avg       0.99      0.99      0.99     11560\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(\"Random Forest classification report: \\n\\n\"  ,classification_report(y_test,y_pred_rf))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "5b5db7a4",
   "metadata": {
    "papermill": {
     "duration": 0.053205,
     "end_time": "2023-09-16T09:20:49.235316",
     "exception": false,
     "start_time": "2023-09-16T09:20:49.182111",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Gradient Boosting classification report: \n",
      "\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "           0       0.99      0.98      0.99      5779\n",
      "           1       0.98      0.99      0.99      5781\n",
      "\n",
      "    accuracy                           0.99     11560\n",
      "   macro avg       0.99      0.99      0.99     11560\n",
      "weighted avg       0.99      0.99      0.99     11560\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(\"Gradient Boosting classification report: \\n\\n\"  ,classification_report(y_test,y_pred_gb))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "7fc073c4",
   "metadata": {
    "papermill": {
     "duration": 0.036387,
     "end_time": "2023-09-16T09:20:49.287713",
     "exception": false,
     "start_time": "2023-09-16T09:20:49.251326",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Logistic Regression Accuracy Score: 0.8992214532871973\n",
      "Decision Tree Accuracy Score:  0.985553633217993\n",
      "Random Forest accuracy score:  0.9908304498269896\n",
      "Gradient Boosting accuracy score:  0.9873702422145328\n"
     ]
    }
   ],
   "source": [
    "print(\"Logistic Regression Accuracy Score:\", accuracy_score(y_test,y_pred))\n",
    "print(\"Decision Tree Accuracy Score: \", accuracy_score(y_test,y_pred_dt))\n",
    "print(\"Random Forest accuracy score: \", accuracy_score(y_test,y_pred_rf))\n",
    "print(\"Gradient Boosting accuracy score: \", accuracy_score(y_test, y_pred_gb))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b9c72270",
   "metadata": {
    "papermill": {
     "duration": 0.015794,
     "end_time": "2023-09-16T09:20:49.320155",
     "exception": false,
     "start_time": "2023-09-16T09:20:49.304361",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Conclusion\n",
    "\n",
    "For the fraud prediction, Random Forest Classification model has the highest accuracy score."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 71.726477,
   "end_time": "2023-09-16T09:20:50.562912",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2023-09-16T09:19:38.836435",
   "version": "2.4.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
