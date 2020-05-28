class ResumeDegree:
    NO_LIMITATION = '不限'
    HIGH_SCHOOL = '中专/高中及以下'
    JUNIOR_COLLEGE = '大专'
    BACHELOR = '本科'
    MASTER = '硕士'
    MBA = 'MBA/EMBA'
    DOCTOR = '博士'
    OTHER = '其他'


class ResumeWorkingExp:
    NO_LIMITATION = '不限'
    INTERN = '在读学生'
    CURRENT_STUDENT = 2
    UNDER_ONE = 3
    ONE_THREE = 4
    THREE_FIVE = 5
    FIVE_TEN = 6
    MORE_THAN_TEN = 7


class ResumeTargetSalary:
    UNDER_TWO_THOUSAND = '2000元/月及以下'
    TWO_FOUR_THOUSAND = '2001-4000元/月'
    FOUR_SIX_THOUSAND = '4001-6000元/月'
    SIX_EIGHT_THOUSAND = '6001-8000元/月'
    EIGHT_TEN_THOUSAND = '8001-10000元/月'
    TEN_FIFTEEN_THOUSAND = '10001-15000元/月'
    FIFTEEN_TWENTYFIVE_THOUSAND = '15001-25000元/月'
    MORE_TWENTYFIVE_THOUSAND = '25000元/月以上'


ZHILIAN_DEGREE_MAPPING = {
    '初中': ResumeDegree.HIGH_SCHOOL,
    '中技': ResumeDegree.HIGH_SCHOOL,
    '高中': ResumeDegree.HIGH_SCHOOL,
    '中专': ResumeDegree.HIGH_SCHOOL,
    '大专': ResumeDegree.JUNIOR_COLLEGE,
    '本科': ResumeDegree.BACHELOR,
    '硕士': ResumeDegree.MASTER,
    'MBA': ResumeDegree.MBA,
    'EMBA': ResumeDegree.MBA,
    '博士': ResumeDegree.DOCTOR,
    '其他': ResumeDegree.OTHER
}

ZHILIAN_WORKING_EXP_MAPPING = {
    '0年工作经验': '3',
    '1年工作经验': '4',
    '2年工作经验': '4',
    '3年工作经验': '4',
    '4年工作经验': '5',
    '5年工作经验': '5',
    '6年工作经验': '6',
    '7年工作经验': '6',
    '8年工作经验': '6',
    '9年工作经验': '6',
    '10年工作经验': '6',
    '10年以上工作经验': '7'
}

ZHILIAN_TARGET_SALARY_MAP_MAPPING = {
    '1000元/月以下': ResumeTargetSalary.UNDER_TWO_THOUSAND,
    '1000-2000元/月': ResumeTargetSalary.UNDER_TWO_THOUSAND,
    '2001-4000元/月': ResumeTargetSalary.TWO_FOUR_THOUSAND,
    '4001-6000元/月': ResumeTargetSalary.FOUR_SIX_THOUSAND,
    '6001-8000元/月': ResumeTargetSalary.SIX_EIGHT_THOUSAND,
    '8001-10000元/月': ResumeTargetSalary.EIGHT_TEN_THOUSAND,
    '10001-15000元/月': ResumeTargetSalary.TEN_FIFTEEN_THOUSAND,
    '15000-25000元/月': ResumeTargetSalary.FIFTEEN_TWENTYFIVE_THOUSAND,
    '25000-35000元/月': ResumeTargetSalary.MORE_TWENTYFIVE_THOUSAND,
    '35000-50000元/月': ResumeTargetSalary.MORE_TWENTYFIVE_THOUSAND,
    '50000-70000元/月': ResumeTargetSalary.MORE_TWENTYFIVE_THOUSAND,
    '70000-100000元/月': ResumeTargetSalary.MORE_TWENTYFIVE_THOUSAND,
    '100000元/月以上': ResumeTargetSalary.MORE_TWENTYFIVE_THOUSAND,
}

FIVEONE_DEGREE_MAPPING = {
    '初中及以下': ResumeDegree.HIGH_SCHOOL,
    '中技': ResumeDegree.HIGH_SCHOOL,
    '中专': ResumeDegree.HIGH_SCHOOL,
    '高中': ResumeDegree.HIGH_SCHOOL,
    '大专': ResumeDegree.JUNIOR_COLLEGE,
    '本科': ResumeDegree.BACHELOR,
    'MBA': ResumeDegree.MBA,
    '硕士': ResumeDegree.MASTER,
    '博士': ResumeDegree.DOCTOR
}

FIVEONE_WORKING_EXP_MAPPING = {
    '在读学生': ResumeWorkingExp.INTERN,
    '应届毕业生': ResumeWorkingExp.CURRENT_STUDENT,
    '1年': ResumeWorkingExp.UNDER_ONE,
    '2年': ResumeWorkingExp.ONE_THREE,
    '3-4年': ResumeWorkingExp.THREE_FIVE,
    '5-7年': ResumeWorkingExp.FIVE_TEN,
    '8-9年': ResumeWorkingExp.FIVE_TEN,
    '10年以上': ResumeWorkingExp.MORE_THAN_TEN
}

FIVEONE_TARGET_SALARY_MAP_MAPPING = {
    '1500以下': ResumeTargetSalary.UNDER_TWO_THOUSAND,
    '1500-1999': ResumeTargetSalary.UNDER_TWO_THOUSAND,
    '2000-2999': ResumeTargetSalary.TWO_FOUR_THOUSAND,
    '3000-4499': ResumeTargetSalary.TWO_FOUR_THOUSAND,
    '4500-5999': ResumeTargetSalary.FOUR_SIX_THOUSAND,
    '6000-7999': ResumeTargetSalary.SIX_EIGHT_THOUSAND,
    '8000-9999': ResumeTargetSalary.EIGHT_TEN_THOUSAND,
    '10000-14999': ResumeTargetSalary.TEN_FIFTEEN_THOUSAND,
    '15000-19999': ResumeTargetSalary.FIFTEEN_TWENTYFIVE_THOUSAND,
    '20000-24999': ResumeTargetSalary.FIFTEEN_TWENTYFIVE_THOUSAND,
    '25000-29999': ResumeTargetSalary.MORE_TWENTYFIVE_THOUSAND,
    '30000-39999': ResumeTargetSalary.MORE_TWENTYFIVE_THOUSAND,
    '40000-49999': ResumeTargetSalary.MORE_TWENTYFIVE_THOUSAND,
    '50000-69999': ResumeTargetSalary.MORE_TWENTYFIVE_THOUSAND,
    '70000-99999': ResumeTargetSalary.MORE_TWENTYFIVE_THOUSAND,
    '100000及以上': ResumeTargetSalary.MORE_TWENTYFIVE_THOUSAND
}

EDUCATION_SORT = {
    '大专': '3',
    '本科': '4',
    '硕士': '5',
    '博士': '6',
    'MBA': '5',
    'EMBA': '5',
    '中专': '2',
    '中技': '2',
    '高中': '2',
    '初中': '1',
    '其他': '1'
}

FIVEONE_CURRENT_STATUS = {
    '目前正在找工作': '1',
    '半年内无换工作的计划': '3',
    '一年内无换工作的计划': '3',
    '观望有好的机会再考虑': '3',
    '我暂时不想找工作': '4'
}

ZHILIAN_CURRENT_STATUS = {
    '我目前处于离职状态，可立即上岗': '1',
    '我目前在职，正考虑换个新环境（如有合适的工作机会，到岗时间一个月左右）': '2',
    '我对现有工作还算满意，如有更好的工作机会，我也可以考虑。（到岗时间另议）': '3',
    '目前暂无跳槽打算': '4',
    '应届毕业生': '1'
}

ZHILIAN_MARRIAGE_STATUS = {
    '未婚': '1',
    '已婚': '4',
    '离异': '2'
}


GENDER_STATUS = {
    u'男': '1',
    u'女': '0'
}

FIVEONE_EXPECT_TYPE = {
    u'全职': 1,
    u'兼职': 2,
    u'实习': 3,
}

bool_dict = {
    '0': u'否',
    '1': u'是'
}

working_exp_dict = {
    '1': u'在读学生',
    '2': u'应届毕业生',
    '3': u'1年以下',
    '4': u'1-3年',
    '5': u'3-5年',
    '6': u'5-10年',
    '7': u'10年以上'
}

work_charact_dict = {
    '1': u'全职',
    '2': u'兼职',
    '3': u'实习'
}

degree_dict = {
    '1': u'初中',
    '2': u'高中/中技/中专',
    '3': u'大专',
    '4': u'本科',
    '5': u'硕士',
    '6': u'博士'
}

DEGREE_51JOB = {
    '不限': '0',
    '初中及以下': '1',
    '高中': '2',
    '中技': '2',
    '中专': '2',
    '大专': '3',
    '本科': '4',
    '硕士': '5',
    '博士': '6',
    'MBA': '6'
}


job_status_dict = {
    '0': u'未开放',
    '1': u'开放中',
    '-1': u'已关闭'
}

job_source_dict = {
    '1': u'魔方招聘',
    '2': u'前程无忧',
    '3': u'智联',
    '4': u'58同城',
    '5': u'拉勾',
    '6': u'中华英才',
    '7': u'赶集招聘',
    '8': u'Boss直聘',
    '9': u'猎聘'
}

current_status_dict = {
    '1': u'目前正在找工作',
    '2': u'在职，正考虑换工作',
    '3': u'在职，只考虑更好的机会',
    '4': u'在职，暂无跳槽打算'
}


company_charact_dict = {
    '1': u'国企',
    '2': u'民营',
    '3': u'合资',
    '4': u'外资',
    '5': u'股份制企业',
    '6': u'上市公司',
    '7': u'代表处',
    '8': u'政府机关事业单位',
    '9': u'非营利机构',
    '10': u'创业公司',
    '99': u'其它'
}

company_scale_dict ={
    '1': u'少于50人',
    '2': u'50-150人',
    '3': u'150-500人',
    '4': u'500-1000人',
    '5': u'1000-10000人',
    '6': u'10000人以上'
}

company_stage_dict ={
    '1': u'未融资',
    '2': u'天使轮',
    '3': u'A轮',
    '4': u'B轮',
    '5': u'C轮',
    '6': u'D轮及以上',
    '7': u'上市公司',
    '8': u'不需要融资'
}

user_marriage_dict = {
    '1': u'未婚',
    '2': u'离异',
    '3': u'丧偶',
    '4': u'已婚'
}
