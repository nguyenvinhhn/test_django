build:
	docker-compose build

up:
	docker-compose up -d

up-non-daemon:
	docker-compose up

start:
	docker-compose start

stop:
	docker-compose stop

restart:
	docker-compose stop && docker-compose start

shell-nginx:
	docker exec -ti nz01 /bin/sh

shell-web:
	docker exec -ti dz01 /bin/sh
# trong shell web tiếp tục vào shell của python \
	python manage.py shell \
		from myapp.models import Question \
		from django.utils import timezone \
			timezone.now() \
		t = timezone.now() \
		t => enter \
		Question.objects.all() \
		q = Question(question_text="ban thich mau gi?", time_pub=t) \
		q.save() lưu vào database \
		c = Choice(question=q, choice_text="xanh", vote=0) \
		c.save() \
		d = Choice(question=q, choice_text="red", vote=0) \
		d.save() \
		Choice.objects.all()

# trong shell-web \
	python manage.py createsuperuser (tạo tài khoản admin của ip/admin) \
		user: user \
		password: password \
	trong admin.py đăng ký thêm model


shell-db:
	docker exec -ti pz01 /bin/sh
	

log-nginx:
	docker-compose logs nginx  

log-web:
	docker-compose logs web  

log-db:
	docker-compose logs db

collectstatic:
	docker exec dz01 /bin/sh -c "python manage.py collectstatic --noinput"  

shell-d-help:
	docker exec dz01 /bin/sh -c "python manage.py"

shell-d-migrate:
	docker exec dz01 /bin/sh -c "python manage.py migrate"

shell-d-makemigrations:
	docker exec dz01 /bin/sh -c "python manage.py makemigrations"
