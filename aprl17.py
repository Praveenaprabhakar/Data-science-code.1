import pandas as pd
import numpy as np
from scipy import stats

data=pd.read_csv("college_admission.csv")
data=data["Gender"]
mean=np.mean(data)
sem=stats.sem(data)
confidence=0.95
n=len(data)

tdis=stats.t.ppf((1+confidence)/2,df=n-1)
marginerror=tdis*sem

l=mean-marginerror
u=mean+marginerror

print(mean,sem,tdis,l,u,sep="\n")
