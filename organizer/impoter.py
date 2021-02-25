import pandas as pd
import sys

sys.path.append('..')
from team.models import Team
# from 大学生比赛评分项目 import settings
def impoter(file_path = r'C:\Users\Administrator\Desktop\大学生比赛评分项目\static\参赛队伍信息模板\参赛队伍信息模板.xlsx'):
    file_path = r'C:\Users\Administrator\Desktop\大学生比赛评分项目\static\参赛队伍信息模板\参赛队伍信息模板.xlsx'
    names = ['team_id', 'team_name', 'competition', 'type', 'group', 'stu_id_1', 'stu_id_2', 'stu_id_3', 'stu_id_4', 'stu_id_5', 'stu_id_6']
    reader = pd.read_excel(file_path, names=names)
    team = {}
    teams = []

    for i in range(0,reader.shape[0]):
        for j in range(0, reader.shape[1]):
            team.update({names[j]:reader.iloc[i,j]})
            
        teams.append(team)

    for i in range(0,len(teams)):
        team_id,team_name,competition,type,group,stu_id_1,stu_id_2, stu_id_3, stu_id_4, stu_id_5, stu_id_6 = [teams[i][j] for j in teams[i]]
    
    return team_id,team_name,competition,type,group,stu_id_1,stu_id_2, stu_id_3, stu_id_4, stu_id_5, stu_id_6

print(impoter())
