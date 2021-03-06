CREATE TABLE CIIU(
   ciiu        VARCHAR(5) NOT NULL PRIMARY KEY
  ,descripcion VARCHAR(174) NOT NULL
);
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('A0112','Cultivo de arroz')
,('A0113','Cultivo de hortalizas  raices y tuberculos')
,('A0119','Otros cultivos transitorios n.c.p.')
,('A0121','Cultivo de frutas tropicales y subtropicales')
,('A0123','Cultivo de cafe')
,('A0126','Cultivo de palma para aceite (palma africana) y otros frutos oleaginosos')
,('A0127','Cultivo de plantas con las que se preparan bebidas')
,('A0128','Cultivo de especias y de plantas aromaticas y medicinales ají  pimiento')
,('A0129','Otros cultivos permanentes n.c.p.')
,('A0130','Propagacion de plantas (actividades de los viveros  excepto viveros forestales)');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('A0141','Cria de ganado bovino y bufalino')
,('A0144','Cria de ganado porcino')
,('A0145','Cria de aves de corral')
,('A0149','Cria de otros animales n.c.p.')
,('A0150','Explotacion mixta (agricola y pecuaria)')
,('A0161','Actividades de apoyo a la agricultura')
,('A0162','Actividades de apoyo a la ganaderia')
,('A0210','Silvicultura y otras actividades forestales')
,('A0220','Extraccion de madera')
,('A0321','Acuicultura maritima');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('A0322','Acuicultura de agua dulce')
,('B0510','Extraccion de hulla (carbon de piedra)')
,('B0811','Extraccion de piedra  arena  arcillas comunes  yeso y anhidrita')
,('B0812','Extraccion de arcillas de uso industrial  caliza  caolin y bentonitas')
,('B0891','Extraccion de minerales para la fabricacion de abonos y productos quimicos')
,('B0899','Extraccion de otros minerales no metalicos n.c.p.')
,('B0910','Actividades de apoyo para la extraccion de petroleo y de gas natural')
,('C1011','Procesamiento y conservacion de carne y productos carnicos')
,('C1020','Procesamiento y conservacion de frutas  legumbres  hortalizas y tuberculos')
,('C1030','Elaboracion de aceites y grasas de origen vegetal y animal');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('C1040','Elaboracion de productos lacteos')
,('C1051','Elaboracion de productos de molineria')
,('C1061','Trilla de cafe')
,('C1062','Descafeinado  tostion y molienda del cafe')
,('C1063','Otros derivados del cafe')
,('C1072','Elaboracion de panela')
,('C1081','Elaboracion de productos de panaderia')
,('C1082','Elaboracion de cacao  chocolate y productos de confiteria')
,('C1084','Elaboracion de comidas y platos preparados')
,('C1089','Elaboracion de otros productos alimenticios n.c.p.');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('C1090','Elaboracion de alimentos preparados para animales')
,('C1101','Destilacion  rectificacion y mezcla de bebidas alcoholicas')
,('C1102','Elaboracion de bebidas fermentadas no destiladas')
,('C1103','Produccion de malta  elaboracion de cervezas y otras bebidas malteadas')
,('C1104','Elaboracion de bebidas no alcoholicas  produccion de aguas minerales y otras aguas embotelladas')
,('C1312','Tejeduria de productos textiles')
,('C1313','Acabado de productos textiles')
,('C1391','Fabricacion de tejidos de punto y ganchillo')
,('C1392','Confeccion de articulos con materiales textiles  excepto prendas de vestir')
,('C1399','Fabricacion de otros articulos textiles n.c.p.');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('C1410','Confeccion de prendas de vestir  excepto prendas de piel')
,('C1511','Curtido y recurtido de cueros  recurtido y tejido de pieles')
,('C1512','Fabricacion de articulos de viaje  bolsos de mano y articulos similares elaborados en cuero  y fabricacion de articulos de talabarteria y guarnicioneria')
,('C1513','Fabricacion de articulos de viaje  bolsos de mano y articulos similares  articulos de talabarteria y guarnicioneria elaborados en otros materiales')
,('C1521','Fabricacion de calzado de cuero y piel  con cualquier tipo de suela')
,('C1610','Aserrado  acepillado e impregnacion de la madera')
,('C1630','Fabricacion de partes y piezas de madera  de carpinteria y ebanisteria para la construccion')
,('C1690','Fabricacion de otros productos de madera  fabricacion de articulos de corcho  cesteria y esparteria')
,('C1811','Actividades de impresion')
,('C1812','Actividades de servicios relacionados con la impresion');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('C1820','Produccion de copias a partir de grabaciones originales')
,('C1921','Fabricacion de productos de la refinacion del petroleo')
,('C2012','Fabricacion de abonos y compuestos inorganicos nitrogenados')
,('C2013','Fabricacion de plasticos en formas primarias')
,('C2021','Fabricacion de plaguicidas y otros productos quimicos de uso agropecuario')
,('C2022','Fabricacion de pinturas  barnices y revestimientos similares  tintas para impresion y masillas')
,('C2023','Fabricacion de jabones y detergentes  preparados para limpiar y pulir  perfumes y preparados de tocador')
,('C2029','Fabricacion de otros productos quimicos n.c.p.')
,('C2030','Fabricacion de fibras sinteticas y artificiales')
,('C2100','Fabricacion de productos farmaceuticos  sustancias quimicas medicinales productos botanicos de uso farmaceutico');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('C2219','Fabricacion de formas basicas de caucho y otros productos de caucho  n.c.p.')
,('C2221','Fabricacion de formas basicas de plastico')
,('C2229','Fabricacion de articulos de plastico n.c.p.')
,('C2310','Fabricacion de vidrio y productos de vidrio')
,('C2392','Fabricacion de materiales de arcilla para la construccion')
,('C2393','Fabricacion de otros productos de ceramica y porcelana')
,('C2395','Fabricacion de articulos de hormigon  cemento y yeso')
,('C2399','Fabricacion de otros productos minerales no metalicos n.c.p.')
,('C2410','Industrias basicas de hierro y de acero')
,('C2421','Industrias basicas de metales preciosos');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('C2429','Industrias basicas de otros metales no ferrosos')
,('C2511','Fabricacion de productos metalicos para uso estructural')
,('C2512','Fabricacion de tanques  depositos y recipientes de metal  excepto los utilizados para el envase o transporte de mercancias')
,('C2520','Fabricacion de armas y municiones')
,('C2592','Tratamiento y revestimiento de metales  mecanizado')
,('C2593','Fabricacion de articulos de cuchilleria  herramientas de mano y articulos de ferreteria')
,('C2599','Fabricacion de otros productos elaborados de metal n.c.p.')
,('C2640','Fabricacion de aparatos electronicos de consumo')
,('C2660','Fabricacion de equipo de irradiacion y equipo electronico de uso medico y terapeutico')
,('C2720','Fabricacion de pilas  baterias y acumuladores electricos');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('C2750','Fabricacion de aparatos de uso domestico')
,('C2825','Fabricacion de maquinaria para la elaboracion de alimentos  bebidas y tabaco')
,('C2910','Fabricacion de vehiculos automotores y sus motores')
,('C2920','Fabricacion de carrocerias para vehiculos automotores  fabricacion de remolques y semirremolques')
,('C3091','Fabricacion de motocicletas')
,('C3110','Fabricacion de muebles')
,('C3210','Fabricacion de joyas  bisuteria y articulos conexos')
,('C3230','Fabricacion de articulos y equipo para la practica del deporte')
,('C3240','Fabricacion de juegos  juguetes y rompecabezas')
,('C3250','Fabricacion de instrumentos  aparatos y materiales medicos y odontologicos (incluido mobiliario)');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('C3290','Otras industrias manufactureras n.c.p.')
,('C3311','Mantenimiento y reparacion especializado de productos elaborados en metal')
,('C3312','Mantenimiento y reparacion especializado de maquinaria y equipo')
,('C3314','Mantenimiento y reparacion especializado de equipo electrico')
,('C3315','Mantenimiento y reparación especializado de equipo de transporte  excepto los vehículos automotores  motocicletas y bicicletas')
,('C3319','Mantenimiento y reparacion de otros tipos de equipos y sus componentes n.c.p.')
,('D3511','Generacion de energia electrica')
,('D3512','Transmision de energia electrica')
,('D3514','Comercializacion de energia electrica')
,('D3520','Produccion de gas  distribucion de combustibles gaseosos por tuberias');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('D3530','Suministro de vapor y aire acondicionado')
,('E3600','Captacion  tratamiento y distribucion de agua')
,('E3700','Evacuacion y tratamiento de aguas residuales')
,('E3811','Recoleccion de desechos no peligrosos')
,('E3812','Recoleccion de desechos peligrosos')
,('E3830','Recuperacion de materiales')
,('E3900','Actividades de saneamiento ambiental y otros servicios de gestion de desechos')
,('F4111','Construccion de edificios residenciales')
,('F4112','Construccion de edificios no residenciales')
,('F4210','Construccion de carreteras y vias de ferrocarril');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('F4220','Construccion de proyectos de servicio publico')
,('F4290','Construccion de otras obras de ingenieria civil')
,('F4311','Demolición')
,('F4312','Preparacion del terreno')
,('F4321','Instalaciones electricas')
,('F4322','Instalaciones de fontaneria  calefaccion y aire acondicionado')
,('F4330','Terminacion y acabado de edificios y obras de ingenieria civil')
,('F4390','Otras actividades especializadas para la construccion de edificios y obras de ingenieria civil')
,('G4511','Comercio de vehiculos automotores nuevos')
,('G4512','Comercio de vehiculos automotores usados');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('G4520','Mantenimiento y reparacion de vehiculos automotores')
,('G4530','Comercio de partes  piezas (autopartes) y accesorios (lujos) para vehiculos automotores')
,('G4541','Comercio de motocicletas y de sus partes  piezas y accesorios')
,('G4542','Mantenimiento y reparacion de motocicletas y de sus partes y piezas')
,('G4610','Comercio al por mayor a cambio de una retribucion o por contrata')
,('G4620','Comercio al por mayor de materias primas agropecuarias  animales vivos')
,('G4631','Comercio al por mayor de productos alimenticios')
,('G4632','Comercio al por mayor de bebidas y tabaco')
,('G4641','Comercio al por mayor de productos textiles  productos confeccionados para uso domestico')
,('G4642','Comercio al por mayor de prendas de vestir');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('G4643','Comercio al por mayor de calzado')
,('G4644','Comercio al por mayor de aparatos y equipo de uso domestico')
,('G4645','Comercio al por mayor de productos farmaceuticos  medicinales  cosmeticos y de tocador')
,('G4649','Comercio al por mayor de otros utensilios domesticos n.c.p.')
,('G4651','Comercio al por mayor de computadores  equipo periferico y programas de informatica')
,('G4652','Comercio al por mayor de equipo  partes y piezas electronicos y de telecomunicaciones')
,('G4653','Comercio al por mayor de maquinaria y equipo agropecuarios')
,('G4659','Comercio al por mayor de otros tipos de maquinaria y equipo n.c.p.')
,('G4661','Comercio al por mayor de combustibles solidos  liquidos  gaseosos y productos conexos')
,('G4662','Comercio al por mayor de metales y productos metaliferos');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('G4663','Comercio al por mayor de materiales de construccion  articulos de ferreteria  pinturas  productos de vidrio  equipo y materiales de fontaneria y calefaccion')
,('G4664','Comercio al por mayor de productos quimicos basicos  cauchos y plasticos en formas primarias y productos quimicos de uso agropecuario')
,('G4665','Comercio al por mayor de desperdicios  desechos y chatarra')
,('G4669','Comercio al por mayor de otros productos n.c.p.')
,('G4690','Comercio al por mayor no especializado')
,('G4711','Comercio al por menor en establecimientos no especializados con surtido compuesto principalmente por alimentos  bebidas o tabaco')
,('G4719','Comercio al por menor en establecimientos no especializados  con surtido compuesto principalmente por productos diferentes de alimentos (viveres en general)  bebidas y tabaco')
,('G4721','Comercio al por menor de productos agricolas para el consumo en establecimientos especializados')
,('G4722','Comercio al por menor de leche  productos lacteos y huevos  en establecimientos especializados')
,('G4723','Comercio al por menor de carnes (incluye aves de corral)  productos carnicos  pescados y productos de mar  en establecimientos especializados');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('G4724','Comercio al por menor de bebidas y productos del tabaco  en establecimientos especializados')
,('G4729','Comercio al por menor de otros productos alimenticios n.c.p.  en establecimientos especializados')
,('G4731','Comercio al por menor de combustible para automotores')
,('G4732','Comercio al por menor de lubricantes (aceites  grasas)  aditivos y productos de limpieza para vehiculos automotores')
,('G4741','Comercio al por menor de computadores  equipos perifericos  programas de informatica y equipos de telecomunicaciones en establecimientos especializados')
,('G4742','Comercio al por menor de equipos y aparatos de sonido y de video  en establecimientos especializados')
,('G4751','Comercio al por menor de productos textiles en establecimientos especializados')
,('G4752','Comercio al por menor de articulos de ferreteria  pinturas y productos de vidrio en establecimientos especializados')
,('G4753','Comercio al por menor de tapices  alfombras y recubrimientos para paredes y pisos en establecimientos especializados')
,('G4754','Comercio al por menor de electrodomesticos y gasodomesticos de uso domestico  muebles y equipos de iluminacion');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('G4755','Comercio al por menor de articulos y utensilios de uso domestico')
,('G4759','Comercio al por menor de otros articulos domesticos en establecimientos especializados')
,('G4761','Comercio al por menor de libros  periodicos  materiales y articulos de papeleria y escritorio  en establecimientos especializados')
,('G4762','Comercio al por menor de articulos deportivos  en establecimientos especializados')
,('G4769','Comercio al por menor de otros articulos culturales y de entretenimiento n.c.p. enestablecimientos especializados')
,('G4771','Comercio al por menor de prendas de vestir y sus accesorios (incluye articulos de piel) en establecimientos especializados')
,('G4772','Comercio al por menor de todo tipo de calzado y articulos de cuero y sucedaneos del cuero en establecimientos especializados')
,('G4773','Comercio al por menor de productos farmaceuticos y medicinales  cosmeticos y articulos de tocador en establecimientos especializados')
,('G4774','Comercio al por menor de otros productos nuevos en establecimientos especializados')
,('G4775','Comercio al por menor de articulos de segunda mano');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('G4781','Comercio al por menor de alimentos  bebidas y tabaco en puestos de venta moviles')
,('G4782','Comercio al por menor de productos textiles  prendas de vestir y calzado  en puestos de venta moviles')
,('G4789','Comercio al por menor de otros productos en puestos de venta moviles')
,('G4791','Comercio al por menor realizado a traves de internet')
,('G4792','Comercio al por menor realizado a traves de casas de venta o por correo')
,('G4799','Otros tipos de comercio al por menor no realizado en establecimientos  puestos de venta o mercados')
,('H4921','Transporte de pasajeros')
,('H4922','Transporte mixto')
,('H4923','Transporte de carga por carretera')
,('H4930','Transporte por tuberias');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('H5111','Transporte aereo nacional de pasajeros')
,('H5210','Almacenamiento y deposito')
,('H5221','Actividades de estaciones  vias y servicios complementarios para el transporte terrestre')
,('H5229','Otras actividades complementarias al transporte')
,('H5310','Actividades postales nacionales')
,('H5320','Actividades de mensajeria')
,('I5511','Alojamiento en hoteles')
,('I5512','Alojamiento en apartahoteles')
,('I5519','Otros tipos de alojamiento para visitantes')
,('I5520','Actividades de zonas de camping y parques para vehiculos recreacionales');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('I5530','Servicio por horas')
,('I5590','Otros tipos de alojamiento n.c.p.')
,('I5611','Expendio a la mesa de comidas preparadas')
,('I5612','Expendio por autoservicio de comidas preparadas')
,('I5613','Expendio de comidas preparadas en cafeterias')
,('I5619','Otros tipos de expendio de comidas preparadas n.c.p.')
,('I5621','Catering para eventos')
,('I5629','Actividades de otros servicios de comidas')
,('I5630','Expendio de bebidas alcoholicas para el consumo dentro del establecimiento')
,('J5811','Edicion de libros');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('J5813','Edicion de periodicos  revistas y otras publicaciones periodicas')
,('J5819','Otros trabajos de edicion')
,('J5911','Actividades de produccion de peliculas cinematograficas  videos  programas  anuncios y comerciales de television')
,('J5914','Actividades de exhibicion de peliculas cinematograficas y videos')
,('J5920','Actividades de grabacion de sonido y edicion de musica')
,('J6010','Actividades de programacion y transmision en el servicio de radiodifusion sonora')
,('J6020','Actividades de programacion y transmision de television')
,('J6110','Actividades de telecomunicaciones alambricas')
,('J6120','Actividades de telecomunicaciones inalambricas')
,('J6130','Actividades de telecomunicacion satelital');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('J6190','Otras actividades de telecomunicaciones')
,('J6201','Actividades de desarrollo de sistemas informaticos (planificacion  analisis  diseño  programacion  pruebas)')
,('J6202','Actividades de consultoria informatica y actividades de administracion de instalaciones informaticas')
,('J6209','Otras actividades de tecnologias de informacion y actividades de servicios informaticos')
,('J6311','Procesamiento de datos  alojamiento (hosting) y actividades relacionadas')
,('J6312','Portales web')
,('J6391','Actividades de agencias de noticias')
,('J6399','Otras actividades de servicio de informacion n.c.p.')
,('K6412','Bancos comerciales')
,('K6492','Actividades financieras de fondos de empleados y otras formas asociativas del sector solidario');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('K6499','Otras actividades de servicio financiero  excepto las de seguros y pensiones n.c.p.')
,('K6511','Seguros generales')
,('K6611','Administracion de mercados financieros')
,('K6612','Corretaje de valores y de contratos de productos basicos')
,('K6621','Actividades de agentes y corredores de seguros')
,('K6629','Evaluacion de riesgos y daños  y otras actividades de servicios auxiliares')
,('L6810','Actividades inmobiliarias realizadas con bienes propios o arrendados')
,('L6820','Actividades inmobiliarias realizadas a cambio de una retribucion o por contrata')
,('M6910','Actividades juridicas')
,('M6920','Actividades de contabilidad  teneduria de libros  auditoria financiera y asesoria tributaria');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('M7010','Actividades de administracion empresarial')
,('M7020','Actividades de consultoria de gestion')
,('M7110','Actividades de arquitectura e ingenieria y otras actividades conexas de consultoria tecnica')
,('M7120','Ensayos y analisis tecnicos')
,('M7210','Investigaciones y desarrollo experimental en el campo de las ciencias naturales y la ingenieria')
,('M7220','Investigaciones y desarrollo experimental en el campo de las ciencias sociales y las humanidades')
,('M7310','Publicidad')
,('M7410','Actividades especializadas de diseño')
,('M7420','Actividades de fotografia')
,('M7490','Otras actividades profesionales  cientificas y tecnicas n.c.p.');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('M7500','Actividades veterinarias')
,('N7710','Alquiler y arrendamiento de vehiculos automotores')
,('N7721','Alquiler y arrendamiento de equipo recreativo y deportivo')
,('N7722','Alquiler de videos y discos')
,('N7729','Alquiler y arrendamiento de otros efectos personales y enseres domesticos n.c.p.')
,('N7730','Alquiler y arrendamiento de otros tipos de maquinaria  equipo y bienes tangibles n.c.p.')
,('N7810','Actividades de agencias de empleo')
,('N7830','Otras actividades de suministro de recurso humano')
,('N7911','Actividades de las agencias de viaje')
,('N7912','Actividades de operadores turisticos');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('N7990','Otros servicios de reserva y actividades relacionadas')
,('N8010','Actividades de seguridad privada')
,('N8020','Actividades de servicios de sistemas de seguridad')
,('N8110','Actividades combinadas de apoyo a instalaciones')
,('N8129','Otras actividades de limpieza de edificios e instalaciones industriales')
,('N8130','Actividades de paisajismo y servicios de mantenimiento conexos')
,('N8211','Actividades combinadas de servicios administrativos de oficina')
,('N8219','Fotocopiado  preparacion de documentos y otras actividades especializadas de apoyo a oficina')
,('N8220','Actividades de centros de llamadas (call center)')
,('N8230','Organizacion de convenciones y eventos comerciales');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('N8292','Actividades de envase y empaque')
,('N8299','Otras actividades de servicio de apoyo a las empresas n.c.p.')
,('O8411','Actividades legislativas de la administracion publica')
,('O8412','Actividades ejecutivas de la administracion publica')
,('O8413','Regulacion de las actividades de organismos que prestan servicios de salud  educativos  culturales y otros servicios sociales  excepto servicios de seguridad social')
,('O8430','Actividades de planes de seguridad social de afiliacion obligatoria')
,('P8511','Educacion de la primera infancia')
,('P8512','Educacion preescolar')
,('P8513','Educacion basica primaria')
,('P8521','Educacion basica secundaria');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('P8523','Educacion media tecnica y de formacion laboral')
,('P8530','Establecimientos que combinan diferentes niveles de educacion')
,('P8541','Educacion tecnica profesional')
,('P8542','Educacion tecnologica')
,('P8543','Educacion de instituciones universitarias o de escuelas tecnologicas')
,('P8544','Educacion de universidades')
,('P8551','Formacion academica no formal')
,('P8552','Enseñanza deportiva y recreativa')
,('P8553','Enseñanza cultural')
,('P8559','Otros tipos de educacion n.c.p.');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('P8560','Actividades de apoyo a la educacion')
,('Q8610','Actividades de hospitales y clinicas  con internacion')
,('Q8621','Actividades de la practica medica  sin internacion')
,('Q8622','Actividades de la practica odontologica')
,('Q8691','Actividades de apoyo diagnostico')
,('Q8692','Actividades de apoyo terapeutico')
,('Q8699','Otras actividades de atencion de la salud humana')
,('Q8730','Actividades de atencion en instituciones para el cuidado de personas mayores y/o discapacitadas')
,('Q8790','Otras actividades de atencion en instituciones con alojamiento')
,('Q8890','Otras actividades de asistencia social sin alojamiento');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('R9001','Creacion literaria')
,('R9002','Creacion musical')
,('R9005','Artes plasticas y visuales')
,('R9006','Actividades teatrales')
,('R9007','Actividades de espectaculos musicales en vivo')
,('R9008','Otras actividades de espectaculos en vivo')
,('R9101','Actividades de bibliotecas y archivos')
,('R9102','Actividades y funcionamiento de museos  conservacion de edificios y sitios historicos')
,('R9200','Actividades de juegos de azar y apuestas')
,('R9311','Gestion de instalaciones deportivas');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('R9312','Actividades de clubes deportivos')
,('R9319','Otras actividades deportivas')
,('R9321','Actividades de parques de atracciones y parques tematicos')
,('R9329','Otras actividades recreativas y de esparcimiento n.c.p.')
,('S9411','Actividades de asociaciones empresariales y de empleadores')
,('S9412','Actividades de asociaciones profesionales')
,('S9491','Actividades de asociaciones religiosas')
,('S9492','Actividades de asociaciones politicas')
,('S9499','Actividades de otras asociaciones n.c.p.')
,('S9511','Mantenimiento y reparacion de computadores y de equipo periferico');
INSERT INTO CIIU(ciiu,descripcion) VALUES
 ('S9512','Mantenimiento y reparacion de equipos de comunicacion')
,('S9521','Mantenimiento y reparacion de aparatos electronicos de consumo')
,('S9522','Mantenimiento y reparacion de aparatos y equipos domesticos y de jardineria')
,('S9524','Reparacion de muebles y accesorios para el hogar')
,('S9529','Mantenimiento y reparacion de otros efectos personales y enseres domesticos')
,('S9601','Lavado y limpieza  incluso la limpieza en seco  de productos textiles y de piel')
,('S9602','Peluqueria y otros tratamientos de belleza')
,('S9603','Pompas funebres y actividades relacionadas')
,('S9609','Otras actividades de servicios personales n.c.p.');
