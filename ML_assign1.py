# loading countries datset
import pandas as pd
import numpy as np
np.set_printoptions(threshold=np.inf)
data=pd.read_csv('Contriesdata.csv')
data.head()
data.columns.values

# performing one way anova to find differences in mean of Service among different regions

import scipy
df=data[["Region","Service"]]
df["Region"].str.strip()
df
grps = pd.unique(df.Region.values)
grps
df_grp = {grp:df['Service'][df.Region == grp] for grp in grps}
df_grp

scipy.stats.f_oneway(df_grp["OCEANIA"],df_grp["BALTICS"],df_grp["NEAR EAST"])

"""
 F_onewayResult(statistic=1.7624159879184491,pvalue=0.21326816149457023)

In this case. p- value > 0.05. Hence we reject the null hypothesis.
Thus, the mean of Service of Regions : Oceania,Baltics,Near East are different

"""

