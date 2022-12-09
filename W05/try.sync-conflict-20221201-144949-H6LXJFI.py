{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'seaborn'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn [2], line 5\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39maltair\u001b[39;00m \u001b[39mas\u001b[39;00m \u001b[39malt\u001b[39;00m\n\u001b[0;32m      4\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39mnumpy\u001b[39;00m \u001b[39mas\u001b[39;00m \u001b[39mnp\u001b[39;00m\n\u001b[1;32m----> 5\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39mseaborn\u001b[39;00m \u001b[39mas\u001b[39;00m \u001b[39msns\u001b[39;00m\n\u001b[0;32m      7\u001b[0m \u001b[39mfrom\u001b[39;00m \u001b[39msklearn\u001b[39;00m\u001b[39m.\u001b[39;00m\u001b[39mmodel_selection\u001b[39;00m \u001b[39mimport\u001b[39;00m train_test_split\n\u001b[0;32m      8\u001b[0m \u001b[39mfrom\u001b[39;00m \u001b[39msklearn\u001b[39;00m\u001b[39m.\u001b[39;00m\u001b[39mnaive_bayes\u001b[39;00m \u001b[39mimport\u001b[39;00m GaussianNB\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'seaborn'"
     ]
    }
   ],
   "source": [
    "from types import GeneratorType\n",
    "import pandas as pd\n",
    "import altair as alt\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.naive_bayes import GaussianNB\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.ensemble import GradientBoostingClassifier\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn import metrics"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.8 64-bit (microsoft store)",
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
   "version": "3.10.8"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "02e944a08bc0c285921295cda56e4095d8d927958b3ee3adba0d9a0ecede1868"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
