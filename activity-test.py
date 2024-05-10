import pandas as pd
from scipy import stats

data = { 
    "Score": [
        17, 9, 9, 14, 8, 11, 6, 10, 13, 13, 10, 14, 13, 12, 14, 19, 9, 10, 15, 14, 11, 12, 12, 9, 12, 8, 10, 9, 14,
        13, 12, 6, 8, 11, 8, 12, 11, 14, 15, 13, 14, 12, 12, 10, 15, 3, 13, 12, 13, 12, 7, 10, 12, 12, 14, 18, 9, 9,
        9, 14, 10, 10, 12, 16, 11, 7, 7, 13, 13, 9, 13, 9, 10, 10, 11, 8, 10, 8, 12, 6, 5, 8, 11, 14, 12, 10, 10, 6,
        13, 9, 15, 15, 12, 13, 11, 12, 12, 14, 8, 13, 14, 10, 13, 12, 13, 17, 12, 15, 14, 8, 11, 15, 12, 15, 12, 10,
        10, 11, 8, 11, 12, 11, 10, 12, 5
    ],
   "Activity" : [
        "None at all", "None at all", "A moderate amount", "None at all", "None at all", "A great deal", "A little", "A little", "A lot", "A moderate amount", "A lot", "A great deal", "A lot", "A moderate amount", "A great deal", "A lot", "None at all", "None at all", "A great deal", "A lot", "A lot", "A lot", "None at all", "A lot", "None at all", "A moderate amount", "A little", "A little", "A lot", "None at all", "A moderate amount", "A little", "None at all", "None at all", "A little", "None at all", "A moderate amount", "A little", "A great deal", "A lot", "A moderate amount", "A lot", "None at all", "None at all", "A moderate amount", "A little", "A great deal", "A moderate amount", "A lot", "A little", "A little", "None at all", "A lot", "None at all", "A little", "A great deal", "A moderate amount", "A little", "A moderate amount", "None at all", "A lot", "A moderate amount", "A moderate amount", "A lot", "A great deal", "None at all", "A great deal", "None at all", "None at all", "A great deal", "A moderate amount", "None at all", "A little", "None at all", "None at all", "A little", "None at all", "None at all", "None at all", "A lot", "None at all", "A moderate amount", "A lot", "A great deal", "None at all", "None at all", "A moderate amount", "A lot", "A little", "A moderate amount", "A great deal", "None at all", "None at all", "A moderate amount", "None at all", "A great deal", "A great deal", "A lot", "A great deal", "A lot", "A lot", "None at all", "A lot", "A little", "A little", "None at all", "A great deal", "A great deal", "None at all", "None at all", "A great deal", "A lot", "A moderate amount", "A lot", "A great deal", "A great deal", "A great deal", "A moderate amount", "A lot", "A moderate amount", "A little", "A moderate amount", "None at all", "A great deal", "A little"
    ]
}


# Create DataFrame
df = pd.DataFrame(data)

# Organize data by group
grouped = df.groupby('Activity')['Score'].apply(list)

# Extract scores for each group
scores_a = grouped['None at all']
scores_b = grouped['A little']
scores_c = grouped['A moderate amount']
scores_d = grouped['A great deal']
scores_e = grouped['A lot']

# Perform one-way ANOVA
f_value, p_value = stats.f_oneway(scores_a, scores_b, scores_c, scores_d, scores_e)

print('F-value:', f_value)
print('P-value:', p_value)