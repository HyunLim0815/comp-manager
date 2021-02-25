from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations = True
 
    def _create_user(self, telephone, email, password, **extra_fields):
        if not telephone:
            raise ValueError("请填入手机号码！")
        if not password:
            raise ValueError("请填入密码!")
        if not email:
            raise ValueError("请输入邮箱")
        
        user = self.model(telephone=telephone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, telephone, email ,password, **extra_fields):
        # extra_fields.setdefault('is_activate', True)
        return self._create_user(telephone, email ,password, **extra_fields)
 
    def create_superuser(self, telephone, email ,password, **extra_fields):
        # extra_fields.setdefault('is_activate', True)
        return self._create_user(telephone, email , password, **extra_fields)

# 重写原有的User模型
class Users(AbstractBaseUser, PermissionsMixin):
    # 建立自定义字段
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True,error_messages={'email':'该邮箱已注册，请登录或尝试找回密码'})
    telephone = models.CharField(max_length=11,
                                 unique=True,
                                 default='11111111111',
                                 error_messages={'telephone':'该手机号已注册，请登录或尝试找回密码'})
    password = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    
    # , help_text={'password':'请使用数字与字母的组合创建长度在8-15的密码，可使用的特殊符号为：@、!、_'}    
    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = [
        # 'telephone',
        'email',
        'password',
    ]
    objects = UserManager()
     
class WX_users(models.Model):
    id = models.CharField(primary_key=True, max_length=125)
    telephone = models.CharField(max_length=11)
    