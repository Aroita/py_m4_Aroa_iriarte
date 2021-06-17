create table app.VEHICULO
(
	id_coche int auto_increment PRYMARY KEY,
	fabricante varchar(200) null,
	modelo varchar(100) null,
	precio int null,
    color varchar(10) null,
    id_motor int null,
)

create table app.MOTOR
(
	id_motor int auto_increment PRIMARY KEY,
	cv int
    combustible varchar(10)null,
	id_coche int null,
    foreign key (id_coche) references VEHICULO (id_coche) on delete set null
);