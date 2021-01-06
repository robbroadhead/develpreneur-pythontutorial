from dpproject.models import Task,lkpStatus
from django.test import Client, TestCase
from django.db import models

class AllTests(TestCase):
    TestName = "Not Defined"
    
    def setUp(self):
        status = lkpStatus()
        status.name = "Complete"
        status.shortname = "COMP"
        status.save()
        status = lkpStatus()
        status.name = "Cancel"
        status.shortname = "CNCL"
        status.save()
        
    def test1(self):
        self.TestName = "My Test"
        self.assertEqual(self.TestName,"My Test")
        
    def test2(self):
        all = lkpStatus.objects.all()
        self.assertEqual(len(all),2)
        status = lkpStatus.objects.get(name='Status One')
        status.name='Done'
        status.save()
        all = lkpStatus.objects.all()
        self.assertEqual(len(all),2)
        status = lkpStatus.objects.get(shortname='SONE')
        self.assertEqual(status.name,'Done')

    def test3(self):
        all = lkpStatus.objects.all()
        self.assertEqual(len(all),2)
