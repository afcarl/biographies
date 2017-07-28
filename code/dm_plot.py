def dm_plot(diff_matrix_name_path, term1, term2=None, term3=None, term4=None, term5=None):
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    d_m = open(diff_matrix_name_path,'r')
    d_m_df = pd.read_csv(d_m)

    term_list = []
    
    if term1 != None:
        s_term1 = str(term1)
        term_list.append(d_m_df[s_term1])
        ax1 = sns.regplot(x='thedate', y=s_term1, data=d_m_df, lowess=True, label=s_term1)
        ax1.legend(loc='best')
        
    if term2 != None:
        s_term2 = str(term2)
        term_list.append(d_m_df[s_term2])
        ax2 = sns.regplot(x='thedate', y=s_term2, data=d_m_df, lowess=True, label=s_term2)
        ax2.legend(loc='best')
        
    if term3 != None:
        s_term3 = str(term3)
        term_list.append(d_m_df[s_term3])
        ax3 = sns.regplot(x='thedate', y=s_term3, data=d_m_df, lowess=True, label=s_term3)
        ax3.legend(loc='best')
    
    if term4 != None:
        s_term4 = str(term4)
        term_list.append(d_m_df[s_term4])
        ax4 = sns.regplot(x='thedate', y=s_term4, data=d_m_df, lowess=True, label=s_term4)
        ax4.legend(loc='best')

    if term5 != None:
        s_term5 = str(term5)
        term_list.append(d_m_df[s_term5])
        ax5 = sns.regplot(x='thedate', y=s_term5, data=d_m_df, lowess=True, label=s_term5)
        ax5.legend(loc='best')
    
    plt.ylabel('Difference')
    plt.xlabel('Year')
    sns.set_context('poster')
    outfile_name = input('Enter filename for figure to be saved as')
    plt.savefig(outfile_name + '.png')
    plt.show()
    