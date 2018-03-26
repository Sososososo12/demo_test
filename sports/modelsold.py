# coding:utf-8

from django.db import models

# Create your models here.

class degree(models.Model):
    degreeid=models.CharField(max_length=1, verbose_name=u"学位代码",primary_key=True)
    degreename = models.CharField(max_length=10, verbose_name=u"学位名称",null=True)

    class Meta:
        verbose_name = u"学位信息"
        verbose_name_plural = verbose_name

class eduback(models.Model):
    edubackid = models.CharField(max_length=1, verbose_name=u"学历代码", primary_key=True)
    edubackname = models.CharField(max_length=10, verbose_name=u"学历名称",null=True)

    class Meta:
        verbose_name = u"学历信息"
        verbose_name_plural = verbose_name

class researcharea(models.Model):
    researchareaid = models.CharField(max_length=9, verbose_name=u"研究方向代码", primary_key=True)
    researchareaname = models.CharField(max_length=30, verbose_name=u"研究方向名称",null=True)

    class Meta:
        verbose_name = u"研究方向信息"
        verbose_name_plural = verbose_name

class city(models.Model):
    cityid = models.CharField(max_length=6, verbose_name=u"城市代码", primary_key=True)
    cityname = models.CharField(max_length=30, verbose_name=u"城市名称",null=True)
    cityprvince = models.CharField(max_length=30, verbose_name=u"省份名称",null=True)
    citycountry = models.CharField(max_length=30, verbose_name=u"国家名称",null=True)

    class Meta:
        verbose_name = u"城市信息"
        verbose_name_plural = verbose_name

class orgtype(models.Model):
    orgtypeid = models.CharField(max_length=2, verbose_name=u"机构类别代码", primary_key=True)
    orgtypename = models.CharField(max_length=30, verbose_name=u"机构类别名称",null=True)

    class Meta:
        verbose_name = u"研究方向信息"
        verbose_name_plural = verbose_name

class organization(models.Model):
    organizationid =models.CharField(max_length=10, verbose_name=u"机构代码", primary_key=True)
    orgname = models.CharField(max_length=30, verbose_name=u"机构名称")
    organtypeid = models.ForeignKey('orgtype', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = u"机构信息"
        verbose_name_plural = verbose_name

class author(models.Model):
    authorid = models.CharField(max_length=17,primary_key=True, verbose_name=u"作者id")
    authorname = models.CharField(max_length=20, verbose_name=u"作者名称",null=True)
    authorresarea = models.ForeignKey('researcharea',on_delete=models.CASCADE,null=True)
    authorcity = models.ForeignKey('city',on_delete=models.CASCADE,null=True)
    authororg = models.ForeignKey('organization',on_delete=models.CASCADE,null=True)
    authordegree = models.ForeignKey('degree',on_delete=models.CASCADE,null=True)
    authoreddu = models.ForeignKey('eduback',on_delete=models.CASCADE,null=True)
    authoraddress = models.CharField(max_length=50, verbose_name=u"通讯地址", null=True)
    authoremail = models.CharField(max_length=50, verbose_name=u"EMAIL", null=True)
    authortel = models.CharField(max_length=20, verbose_name=u"联系电话", null=True)

    class Meta:
        verbose_name = u"作者信息"
        verbose_name_plural = verbose_name

class journal(models.Model):
    journalid = models.CharField(max_length=8, verbose_name=u"期刊代码", primary_key=True)
    journalname = models.CharField(max_length=20, verbose_name=u"标题",null=True)
    journalnum = models.CharField(max_length=20, verbose_name=u"刊号",null=True)
    majorhostorg = models.ForeignKey('organization',on_delete=models.CASCADE,null=True)
    # vicehostorg = models.ForeignKey('organization',on_delete=models.CASCADE,null=True)#只能有一个外间接入所以指定主承办单位
    becity = models.ForeignKey('city',on_delete=models.CASCADE,null=True)
    majordirector = models.ForeignKey('author',on_delete=models.CASCADE,null=True)
    launchdate = models.CharField(max_length=20, verbose_name=u"创刊时间", null=True)
    authoraddress = models.CharField(max_length=50, verbose_name=u"通讯地址", null=True)
    authoremail = models.CharField(max_length=50, verbose_name=u"EMAIL", null=True)
    authortel = models.CharField(max_length=20, verbose_name=u"联系电话", null=True)
    coretype = models.CharField(max_length=1, verbose_name=u"核心期刊类型", null=True)

    class Meta:
        verbose_name = u"期刊信息"
        verbose_name_plural = verbose_name

class paper(models.Model):
    paperid = models.CharField(max_length=20, verbose_name=u"文献代码", primary_key=True)
    title = models.CharField(max_length=30, verbose_name=u"文献标题",null=True)
    vicetitle = models.CharField(max_length=30, verbose_name=u"文献副标题",null=True)
    paperauthor = models.ForeignKey('author',on_delete=models.CASCADE,null=True)
    # translator = models.ForeignKey('author',on_delete=models.CASCADE,null=True)
    paperauthororg = models.CharField(max_length=200,verbose_name=u"文献作者隶属组织",null=True)
    bejournalid = models.ForeignKey('journal',on_delete=models.CASCADE,null=True)
    pagetype = models.CharField(max_length=8, verbose_name=u"版类",null=True)
    publicdate = models.CharField(max_length=20, verbose_name=u"年份", null=True)
    journalversion = models.CharField(max_length=8, verbose_name=u"源刊期号",null=True)
    journalpages = models.CharField(max_length=8, verbose_name=u"源刊页号",null=True)
    subject= models.CharField(max_length=8, verbose_name=u"学科",null=True)

    class Meta:
        verbose_name = u"文献信息"
        verbose_name_plural = verbose_name

class translator(models.Model):
    translatorid = models.CharField(max_length=10, verbose_name=u"机构代码", primary_key=True)
    translatorname = models.CharField(max_length=30, verbose_name=u"译者名称")
    transpaper = models.ForeignKey('paper', on_delete=models.CASCADE, null=True)


    class Meta:
        verbose_name = u"译者信息"
        verbose_name_plural = verbose_name


