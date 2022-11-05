--
-- PostgreSQL database dump
--

-- Dumped from database version 15.0
-- Dumped by pg_dump version 15.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: bot_database; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE bot_database WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';


ALTER DATABASE bot_database OWNER TO postgres;

\connect bot_database

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: schedule; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.schedule (
    id integer NOT NULL,
    auditorium character varying(10),
    discipline character varying(100) NOT NULL,
    date character varying(12) NOT NULL,
    "beginLesson" character varying(6),
    "endLesson" character varying(6),
    "kindOfWork" character varying(250),
    lecturer character varying(250),
    lecturer_email character varying(250),
    zoom_url character varying(350),
    "dayOfWeekString" character varying(3)
);


ALTER TABLE public.schedule OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    tg_id integer NOT NULL,
    group_id integer NOT NULL,
    username character varying(25) NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Data for Name: schedule; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.schedule (id, auditorium, discipline, date, "beginLesson", "endLesson", "kindOfWork", lecturer, lecturer_email, zoom_url, "dayOfWeekString") FROM stdin;
87481	online	Основы и методология программирования (анг)	2022.11.05	11:10	12:30	Практическое занятие	Рудаков Кирилл Александрович	krudakov@hse.ru	https://us06web.zoom.us/j/83057338860?pwd=dFlsWVZyd0x0RE9uSXJkeFAwOGFnZz09	Сб
93807	online	Линейная алгебра и геометрия (анг)	2022.11.05	14:40	16:00	Контрольная работа	Мажуга Андрей Михайлович	amazhuga@hse.ru		Сб
81589	online	Линейная алгебра и геометрия (анг)	2022.11.05	16:20	17:40	Контрольная работа	Мажуга Андрей Михайлович	amazhuga@hse.ru		Сб
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (tg_id, group_id, username) FROM stdin;
\.


--
-- Name: schedule schedule_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.schedule
    ADD CONSTRAINT schedule_pk PRIMARY KEY (id);


--
-- Name: schedule_id_uindex; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX schedule_id_uindex ON public.schedule USING btree (id);


--
-- PostgreSQL database dump complete
--

