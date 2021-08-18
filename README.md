# [jabbariao.com](https://jabbariao.com) Core

## About

This is my Django API for my personal website. Currently I'm running a Node API in production, but I'm going to end up switching that out for this.

Why? I wanted more practice with Django.

## Technology Used

* [Poetry](https://python-poetry.org/)
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Supabase.io](https://supabase.io)
* [PostgreSQL](https://www.postgresql.org/)

## Can I use this for myself?

Yea. The code here is pretty much just boilerplate for a blog type website. Nothing super specific except that you have to configure your own supabase instance.

## How do I run this?

This assumes you have `poetry` installed on your machine.

### Installing Dependencies

`poetry install`

### Creating Migrations

`poetry run makemigrations`

### Running Migrations

`poetry run migrations`

### Running the Application

`poetry run start`