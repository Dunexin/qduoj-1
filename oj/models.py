from django.db import models

class User(models.Model):	
	user_id = models.CharField(max_length=50, primary_key=True)
	nick = models.CharField(max_length=50)
	password = models.CharField(max_length=100)
	email = models.EmailField(null=True, blank=True)
	isManager = models.IntegerField(default=5)
	website = models.CharField(max_length=50)
	ac = models.IntegerField(default=0)
	submit = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.nick

class Problem(models.Model):
	problem_id = models.AutoField(primary_key=True)
	title = models.TextField()
	description = models.TextField()
	input_data = models.TextField()
	output_data = models.TextField()
	sample_input = models.TextField()
	sameple_output = models.TextField()
	source = models.TextField(null=True, blank=True)
	hint = models.TextField(null=True, blank=True)
	in_date = models.DateTimeField(auto_now_add=True)
	time_limit = models.IntegerField()
	memory_limit = models.IntegerField()
	hard = models.IntegerField()
	accepted = models.IntegerField(default=0)
	submit = models.IntegerField(default=0)
	visible = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.title

class Solution(models.Model):
	solution_id = models.AutoField(primary_key=True)
	problem = models.ForeignKey('Problem')
	user = models.ForeignKey('User')
	score = models.IntegerField()
	time = models.IntegerField()
	memory = models.IntegerField()
	in_date = models.DateTimeField(auto_now_add=True)
	result = models.IntegerField(default=0)
	language = models.IntegerField(default=0)
	judgetime = models.DateTimeField(auto_now_add=False)
	code_length = models.IntegerField()
	
	def __unicode__(self):
		return self.solution_id

class Source_code(models.Model):
	solution_id = models.IntegerField(primary_key=True)
	code = models.TextField()
	
	def __unicode__(self):
		return self.solution_id

class Compileinfo(models.Model):
	solution_id = models.IntegerField(primary_key=True)
	error = models.TextField()
	
	def __unicode__(self):
		return self.solution_id

class LoginLog(models.Model):
	user = models.ForeignKey('User')
	ip = models.IPAddressField()
	time = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.user.nick

class News(models.Model):
	title = models.TextField()
	content = models.TextField()
	time = models.DateTimeField()

	def __unicode__(self):
		return self.title

class Mail(models.Model):
	mail_id = models.IntegerField(primary_key=True)
	mail_to = models.CharField(max_length=50)
	mail_from = models.CharField(max_length=50)
	title = models.TextField()
	content = models.TextField()
	is_new = models.BooleanField(default=False)
	in_date = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.mail_id

class Bbs(models.Model):
	problem = models.ForeignKey('Problem')
	user = models.ForeignKey('User')
	time = models.DateTimeField(auto_now_add=True)	
	text = models.TextField()
	reply_id = models.IntegerField() #if the id == 0, this reply is to the LZ, else to the flaw

	def __unicode__(self):
		return self.problem.problem_id
