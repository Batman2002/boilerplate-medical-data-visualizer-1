import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data

# df2

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.


# Draw Categorical Plot
def draw_cat_plot():
    df=pd.read_csv("medical_examination.csv",index_col="id")

# Add 'overweight' column
    df=pd.read_csv("medical_examination.csv")
    df2=pd.read_csv("medical_examination.csv")
    df3=pd.read_csv("medical_examination.csv")
    df4=pd.read_csv("medical_examination.csv")
    df3.loc[df3["cholesterol"]==1]=0
    df3.loc[df3["cholesterol"]>1]=1
    df4.loc[df4["gluc"]==1]=0
    df4.loc[df4["gluc"]>1]=1
    df["overweight"]=(df["weight"]/((df["height"]/100)**2))
    df.loc[df["overweight"]<=25]=0
    df.loc[df["overweight"]>25]=1
    df2["overweight"]=df["overweight"]
    df2["cholesterol"]=df3["cholesterol"]
    df2["gluc"]=df4["gluc"]
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat=df2.melt(id_vars=["cardio"],value_vars=["cholesterol","gluc","smoke","alco","active","overweight"])
    df_cat["total"]=df_cat["value"]
    df_cat=df_cat.groupby(["cardio","variable","value"]).count()
    # dfcat=df_cat.copy()ctyvvhvcytv uj
    df_cat=df_cat.reset_index()
    df_cat.sort_values("total",ascending=False)
    df_cat["value"]=df_cat["value"].astype(str)
    df_cat["cardio"]=df_cat["cardio"].astype(str)
    df_cat
    fig=sns.catplot(data=df_cat,x="variable",y="total",col="cardio",hue="value",kind="bar").fig
    # df_cat
    # dadwed


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # df_cat = None
    

    # Draw the catplot with 'sns.catplot()'



    # Get the figure for the output
    # fig = None


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    df=pd.read_csv("medical_examination.csv",index_col="id")

# Add 'overweight' column
    df=pd.read_csv("medical_examination.csv")
    df2=pd.read_csv("medical_examination.csv")
    df3=pd.read_csv("medical_examination.csv")
    df4=pd.read_csv("medical_examination.csv")
    df3.loc[df3["cholesterol"]==1]=0
    df3.loc[df3["cholesterol"]>1]=1
    df4.loc[df4["gluc"]==1]=0
    df4.loc[df4["gluc"]>1]=1
    df["overweight"]=(df["weight"]/((df["height"]/100)**2))
    df.loc[df["overweight"]<=25]=0
    df.loc[df["overweight"]>25]=1
    df2["overweight"]=df["overweight"]
    df2["cholesterol"]=df3["cholesterol"]
    df2["gluc"]=df4["gluc"]
    s=(df2['ap_lo'] >= df2['ap_hi'])
    d=df2.loc[s]
    df2.drop(d.index,inplace=True)
    c=(df2['height'] <= df2['height'].quantile(0.025))
    a=(df2['height'] >= df2['height'].quantile(0.975))
    b=df2.loc[a]
    d=df2.loc[c]
    df2.drop(b.index,inplace=True)
    df2.drop(d.index,inplace=True)
    g=(df2['weight'] <= df2['weight'].quantile(0.025))
    f=(df2['weight'] >= df2['weight'].quantile(0.975))
    j=df2.loc[f]
    k=df2.loc[g]
    df2.drop(j.index,inplace=True)
    df2.drop(k.index,inplace=True)
    df2=df2.round(decimals=1)
    # df2=df2.astype('int64')
    corr=df2.corr()
    mask = np.triu(np.ones_like(corr))
    
    # Clean the data
    # df_heat = None

    # Calculate the correlation matrix
    # corr = None

    # Generate a mask for the upper triangle
    # mask = None

    x=sns.heatmap(corr,mask=mask)
    # Set up the matplotlib figure
    fig, ax = plt.subplots()
    ax.plot(data=x)
    
    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
