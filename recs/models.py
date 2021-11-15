from django.db import models

# Create your models here.

class Worker(models.Model):
    pass


class Section1_1(models.Model):
    timestamp = models.DateField(auto_now=True, null=True, blank=True)
    title = '水酸化ナトリウムを秤量する'
    loc = 'section 1-1'

    check1 = models.BooleanField(default=False)
    iText1 = '1 Lジョッキに水 300 mL を入れる。'
    aQty1 = models.FloatField()
    aItemID1 = models.CharField(max_length=25)
    # itemID1 = models.ForeingKey('Item'), on_delete=models.Do_Nothing

    check2 = models.BooleanField(default=False)
    iText2 = '水酸化ナトリウム (Lot. b046) を 4.0 g 秤量する。'
    aItemID2 = models.CharField(max_length=25)
    aQty2 = models.FloatField(blank=False, null=False)
    

    def __str__(self):
        return self.title
        pass
    
class Section1_2(models.Model):
    TimeStamp = models.DateField(auto_created=True)
    title = '1M 塩化水素溶液で滴定する'
    loc = 'section 1-2'

    check1 = models.BooleanField(default=False)
    iText1 = '5 mL ピペットを用意する'
    # aQty1 = models.FloatField()
    aItemID1 = models.CharField(max_length=25)
    itemID1 = models.CharField(max_length=25)

    check2 = models.BooleanField(default=False)
    iText2 = '1M 塩化水素溶液 (Lot. a23) で滴定する'
    aItemID2 = models.CharField(max_length=25)
    aQty2 = models.FloatField(blank=False, null=False)
    

    def __str__(self):
        return self.title
        pass

class Section1_3(models.Model):
    TimeStamp = models.DateField(auto_created=True)
    title = 'リトマス紙で液性を確認する'
    loc = 'section 1-3'

    check1 = models.BooleanField(default=False)
    iText1 = 'リトマス紙を用意する'
    # aQty1 = models.FloatField()
    aItemID1 = models.CharField(max_length=25)
    # itemID1 = models.ForeingKey('Item'), on_delete=models.Do_Nothing

    check2 = models.BooleanField(default=False)
    iText2 = '中性付近の色であることを確認する'
    # aItemID2 = models.CharField(max_length=25)
    # aQty2 = models.FloatField(blank=False, null=False)
    

    def __str__(self):
        return self.title
        pass