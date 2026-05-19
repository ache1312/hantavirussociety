---
title: "Revisión de requisitos 1-25"
subtitle: "Hantavirus Society / ICH2026"
author: "Preparado para revisión de Nicole y equipo"
date: "19 de mayo de 2026"
lang: es-CL
---

![](assets/images/ui/logo.png){width=1.45in}

# Revisión de requisitos 1-25

**Proyecto:** sitio institucional Hantavirus Society e ICH2026  
**Repositorio:** `ache1312/hantavirussociety`  
**Commit de implementación publicado:** `5194a79`  
**Alcance:** revisión de los primeros 25 requisitos levantados desde las observaciones de Nicole.  

## Resumen ejecutivo

La revisión confirma que los primeros 25 requisitos fueron abordados en el sitio. De ellos, 24 se encuentran resueltos o resueltos con nota editorial/técnica, y 1 queda pendiente exclusivamente por falta de insumo externo: la lista confirmada de hoteles cercanos al aeropuerto de Santiago.

| Indicador | Resultado |
|---|---:|
| Requisitos revisados | 25 |
| Resueltos | 21 |
| Resueltos con nota | 3 |
| Pendientes por insumo | 1 |
| Validación automática del sitio | Aprobada |

## Criterios de estado

**Resuelto:** implementado y validado en el sitio o en su generador.  
**Resuelto con nota:** implementado, pero con una aclaración editorial, de fuente o de reemplazo futuro.  
**Pendiente por insumo:** no depende de desarrollo; requiere información confirmada por la organización.

## Matriz de trazabilidad

| # | Área | Estado | Requisito | Resolución |
|---:|---|---|---|---|
| 1 | Society | Resuelto | About ISH debe dar más protagonismo al logo, similar a Sponsors. | Se agregó un bloque institucional destacado con el logo grande al inicio de About ISH. |
| 2 | Society | Resuelto con nota | La imagen viral de About ISH debe incluir referencia, posiblemente CDC / Goldsmith 1995. | Se agregó el crédito visible como "Image reference: CDC / Cynthia Goldsmith, 1993." La fecha 1995 no coincide con la fecha de creación registrada por CDC PHIL, por lo que se dejó la referencia verificada. |
| 3 | Society | Resuelto con nota | Cambiar foto de Piet Maes. | Se cambió desde `board/piet-maes.jpg` a `ich2026/scientific-piet-maes.jpg`, usando el asset disponible. Si llega una nueva foto oficial, se puede reemplazar directamente. |
| 4 | Society | Resuelto | Las fotos del board estaban chicas y con demasiado marco blanco. | Se redujo el borde blanco y se aumentó el tamaño visual de las fotos destacadas. |
| 5 | Society | Resuelto | Connie Schmaljohn debe ir abajo al medio. | Se agregó una clase específica para centrar su tarjeta en desktop/tablet, manteniendo lectura normal en mobile. |
| 6 | Society | Resuelto | Revisar links repetidos del footer/contacto. | Se reorganizó el footer en enlaces de sitio y contactos/acciones, evitando duplicar Contact, Conference form y Contact ICH2026 como items ambiguos. |
| 7 | Society | Resuelto | Agregar "contact ISH: ish@hantavirussociety.org" abajo. | Se agregó en footer y en la sección Contact como contacto institucional ISH. |
| 8 | Society | Resuelto | Incluir pestaña "Former Meetings". | Se creó la página `former-meetings/` con bloque de lectureship awards, archivo histórico por edición, enlaces a abstract books disponibles y galería visual recuperada desde el ZIP. |
| 9 | Society | Resuelto | Incluir pestaña "Communications". | Se agregó la pestaña y página `communications/` con Statement, WHO health topic, evento OMS Andes Virus MCM y webinar PHA4GE. |
| 10 | Society | Resuelto | Communications debe incluir Statement. | Se agregó el PDF `Statement_ISH_Andes_v4.pdf` recuperado desde el ZIP y se dejó un resumen institucional en la página. |
| 11 | Society | Resuelto | Communications debe incluir News from WHO. | Se agregó el enlace a `https://www.who.int/health-topics/hantavirus#tab=tab_1`. |
| 12 | Society | Resuelto | Communications debe incluir WHO meeting last week y notar que la Sociedad pudo moderar el primer bloque. | Se agregó el evento OMS de 2026-05-15 y se indicó que la Session 1 fue chaired by Nicole Tischler, según agenda del evento revisada localmente. |
| 13 | Society | Resuelto | Communications debe incluir webinar PHA4GE sobre secuenciación. | Se agregó el enlace al webinar PHA4GE sobre hantavirus y epidemiología genómica. |
| 14 | Society | Resuelto | Agregar próximo webinar OMS. | Se agregó "Hantavirus in Focus I: what we know and what it means", programado para el 20 de mayo de 2026, como noticia principal en Communications. |
| 15 | Conference | Resuelto | ICH2026 tiene un logo parecido y dos imágenes del lugar adjuntas. | Se rescató desde `Webpage-20260519T141114Z-3-001.zip` la ilustración `ICH2026_V4_landscape_recorte.png` y varias imágenes de Puerto Varas para el hero/galería del congreso. |
| 16 | Conference | Resuelto | Primera página ICH2026 debería incorporar el logo del meeting. | Se incorporó la ilustración/logo del meeting en el hero de ICH2026 como marca visual destacada. |
| 17 | Conference | Resuelto | Antes había un carrusel para atractivos turísticos. | Se agregó una galería responsive con imágenes de Puerto Varas, Osorno y Lake District recuperadas desde el ZIP. La versión actual evita scroll horizontal y muestra las imágenes como grilla adaptable. |
| 18 | Conference | Resuelto | Quitar o cambiar "Choose sessions", porque el meeting es chico. | Se reemplazó por una ruta de información más directa: Scientific Program ICH2026, ANDV Workshop, Keynote Speakers y Abstract Submission Registration. |
| 19 | Conference | Resuelto | Ordenar puntos 1-4 como Scientific Program ICH2026, ANDV Workshop, Keynote Speakers, Abstract Submission Registration. | Se implementó ese orden en el bloque de ruta y en los módulos visuales principales de ICH2026. |
| 20 | Conference | Resuelto con nota | Revisar si dejar las mismas fotos de los cuatro módulos. | Se revisaron los assets disponibles del ZIP y no había nuevas imágenes específicas para esos cuatro módulos. Se mantuvieron las imágenes generadas ya existentes porque son atingentes a las secciones. |
| 21 | Conference | Resuelto | Keynotes OK. | Se mantuvo la página Keynotes sin cambios estructurales, respetando la observación de que estaba correcta. |
| 22 | Conference | Resuelto | Programme no debería repetir la foto de la sociedad. | Se cambió el hero de Programme a una imagen científica de hantavirus, evitando repetir la foto de archivo de la sociedad. |
| 23 | Conference | Resuelto | Venue está bien, pero algunos Travel resources deberían incorporarse más arriba. | Se agregaron accesos destacados a Survip Puerto Montt -> Puerto Varas y transfer SCL/Santiago dentro del primer bloque de Venue. |
| 24 | Conference | Resuelto | El transfer email no se entiende que es en Santiago. | Se renombraron y aclararon los recursos como Santiago/SCL transfer y se diferenciaron de Survip Puerto Montt -> Puerto Varas. |
| 25 | Conference | Pendiente por insumo | Faltan hoteles cerca del aeropuerto de Santiago. | Se agregó una nota indicando que la lista de hoteles cerca de SCL será incorporada cuando la organización la confirme. Este punto no está bloqueado técnicamente, pero requiere información externa. |

## Observaciones de cierre

Los puntos con nota no bloquean el sitio: corresponden a decisiones de fuente, fotografía oficial o criterio editorial. El único punto pendiente real es la información hotelera cerca del aeropuerto de Santiago, que debe ser confirmada por la organización antes de cerrar el requisito 25.

La validación automática del sitio fue ejecutada correctamente con resultado aprobado: `Site validation passed.`
