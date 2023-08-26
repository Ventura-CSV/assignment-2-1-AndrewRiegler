def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    male_students = int(input('Enter the number of male students'))
    female_students = int(input(' Enter the number of female students'))
    
    #male 40#
    #female 60#


    total = male_students + female_students
    m_perc = male_students / total
    f_perc = female_students / total

    print (f'Total number of students: {total}')
    print (f'The number of males and females: {male_students} {female_students}')
    print (f'The percentage of males and females: {m_perc: .2%} {f_perc: .2%}')

    
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
