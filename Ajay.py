{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1225a2bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd # import pandas lib for python\n",
    "d=pd.read_csv(\"C:\\\\Users\\\\Admin\\\\Desktop\\\\data.csv\") # read the file location\n",
    "df=pd.DataFrame(d)#form data frame\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "947e599f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         1278077545  43892.99000000  0.00158000  69.35092420  1646265600000  \\\n",
      "0        1278077546        43892.99     0.00066    28.969373  1646265600000   \n",
      "1        1278077547        43892.98     0.00136    59.694453  1646265600000   \n",
      "2        1278077548        43892.99     0.00045    19.751846  1646265600000   \n",
      "3        1278077549        43892.98     0.00048    21.068630  1646265600001   \n",
      "4        1278077550        43892.99     0.00029    12.728967  1646265600001   \n",
      "...             ...             ...         ...          ...            ...   \n",
      "1289314  1279366860        42454.01     0.00124    52.642972  1646351999996   \n",
      "1289315  1279366861        42454.00     0.00257   109.106780  1646351999996   \n",
      "1289316  1279366862        42454.01     0.00054    22.925165  1646351999997   \n",
      "1289317  1279366863        42454.01     0.00198    84.058940  1646351999997   \n",
      "1289318  1279366864        42454.00     0.00052    22.076080  1646351999999   \n",
      "\n",
      "         False  True  \n",
      "0        False  True  \n",
      "1         True  True  \n",
      "2        False  True  \n",
      "3         True  True  \n",
      "4        False  True  \n",
      "...        ...   ...  \n",
      "1289314  False  True  \n",
      "1289315   True  True  \n",
      "1289316  False  True  \n",
      "1289317  False  True  \n",
      "1289318   True  True  \n",
      "\n",
      "[1289319 rows x 7 columns]\n"
     ]
    }
   ],
   "source": [
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0b34ca4a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "e=pd.read_csv(\"C:\\\\Users\\\\Admin\\\\Desktop\\\\data2.csv\")\n",
    "df=pd.DataFrame(e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d7c465b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         1276424414  44421.20000000  0.00097000  43.08856400  1646179200000  \\\n",
      "0        1276424415        44423.46     0.00154    68.412128  1646179200002   \n",
      "1        1276424416        44423.46     0.00039    17.325149  1646179200003   \n",
      "2        1276424417        44421.20     0.00328   145.701536  1646179200003   \n",
      "3        1276424418        44423.46     0.00075    33.317595  1646179200005   \n",
      "4        1276424419        44423.46     0.00276   122.608750  1646179200007   \n",
      "...             ...             ...         ...          ...            ...   \n",
      "1653125  1278077540        43892.98     0.00040    17.557192  1646265599998   \n",
      "1653126  1278077541        43892.98     0.00159    69.789838  1646265599999   \n",
      "1653127  1278077542        43892.99     0.00064    28.091514  1646265599999   \n",
      "1653128  1278077543        43892.98     0.00054    23.702209  1646265599999   \n",
      "1653129  1278077544        43892.98     0.00061    26.774718  1646265599999   \n",
      "\n",
      "          True  True.1  \n",
      "0        False    True  \n",
      "1        False    True  \n",
      "2         True    True  \n",
      "3        False    True  \n",
      "4        False    True  \n",
      "...        ...     ...  \n",
      "1653125   True    True  \n",
      "1653126   True    True  \n",
      "1653127  False    True  \n",
      "1653128   True    True  \n",
      "1653129   True    True  \n",
      "\n",
      "[1653130 rows x 7 columns]\n"
     ]
    }
   ],
   "source": [
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "19961c1f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "march3=pd.read_csv(\"C:\\\\Users\\\\Admin\\\\Desktop\\\\data3.csv\")\n",
    "df=pd.DataFrame(march3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "72e5fce1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         1278077545  43892.99000000  0.00158000  69.35092420  1646265600000  \\\n",
      "0        1278077546        43892.99     0.00066    28.969373  1646265600000   \n",
      "1        1278077547        43892.98     0.00136    59.694453  1646265600000   \n",
      "2        1278077548        43892.99     0.00045    19.751846  1646265600000   \n",
      "3        1278077549        43892.98     0.00048    21.068630  1646265600001   \n",
      "4        1278077550        43892.99     0.00029    12.728967  1646265600001   \n",
      "...             ...             ...         ...          ...            ...   \n",
      "1289314  1279366860        42454.01     0.00124    52.642972  1646351999996   \n",
      "1289315  1279366861        42454.00     0.00257   109.106780  1646351999996   \n",
      "1289316  1279366862        42454.01     0.00054    22.925165  1646351999997   \n",
      "1289317  1279366863        42454.01     0.00198    84.058940  1646351999997   \n",
      "1289318  1279366864        42454.00     0.00052    22.076080  1646351999999   \n",
      "\n",
      "         False  True  \n",
      "0        False  True  \n",
      "1         True  True  \n",
      "2        False  True  \n",
      "3         True  True  \n",
      "4        False  True  \n",
      "...        ...   ...  \n",
      "1289314  False  True  \n",
      "1289315   True  True  \n",
      "1289316  False  True  \n",
      "1289317  False  True  \n",
      "1289318   True  True  \n",
      "\n",
      "[1289319 rows x 7 columns]\n"
     ]
    }
   ],
   "source": [
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c18db535",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
