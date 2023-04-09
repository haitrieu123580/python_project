from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self):
        return self.name


class Laptop(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    graphic_card = models.CharField(max_length=50)
    ram = models.IntegerField()
    cpu = models.CharField(max_length=50)
    screen_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(null = True, blank = True)
    description = models.CharField(max_length=100, blank=True)
    laptop = models.ForeignKey(
        Laptop, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"Image {self.id}: {self.description}"


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # created_at: trường này là một trường kiểu ngày giờ (datetime field) được tạo tự động khi một bản ghi được tạo ra (auto_now_add).
    # modified_at: trường này là một trường kiểu ngày giờ (datetime field) được cập nhật tự động mỗi khi một bản ghi được lưu lại (auto_now).
    total = models.DecimalField(max_digits=8, decimal_places=2)


class CartItem(models.Model):
    card = models.ForeignKey(Cart, on_delete=models.CASCADE)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.id}: {self.laptop.name} x {self.quantity} ({self.price})"

# để tạo các bảng tương ứng trong cơ sở dữ liệu của bạn
# python manage.py makemigrations
# python manage.py migrate
