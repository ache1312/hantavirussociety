# Bitacora de observaciones Nicole

Fecha: 2026-05-19

## Society

1. Requisito: About ISH debe dar mas protagonismo al logo, similar a Sponsors.
   Resolucion: implementado. Se agrego un bloque institucional destacado con el logo grande al inicio de About ISH.

2. Requisito: la imagen viral de About ISH debe incluir referencia, posiblemente CDC / Goldsmith 1995.
   Resolucion: implementado. Se verifico la referencia contra el archivo local, Pixnio y CDC PHIL. El credito visible quedo como "Image reference: CDC / Cynthia Goldsmith, 1993."; la mencion 1995 no coincide con la fecha de creacion registrada por CDC PHIL.

3. Requisito: cambiar foto de Piet Maes.
   Resolucion: implementado con asset disponible. Se cambio desde `board/piet-maes.jpg` a `ich2026/scientific-piet-maes.jpg`. Si Nicole envia una nueva foto oficial, se reemplaza ese archivo o referencia.

4. Requisito: las fotos del board estaban chicas y con demasiado marco blanco.
   Resolucion: implementado. Se redujo el borde blanco y se aumento el tamano visual de las fotos destacadas.

5. Requisito: Connie Schmaljohn debe ir abajo al medio.
   Resolucion: implementado. Se agrego una clase especifica para centrar su tarjeta en desktop/tablet, manteniendo lectura normal en mobile.

6. Requisito: revisar links repetidos del footer/contacto.
   Resolucion: implementado. Se reorganizo el footer en enlaces de sitio y contactos/acciones, evitando duplicar Contact, Conference form y Contact ICH2026 como items ambiguos.

7. Requisito: agregar "contact ISH: ish@hantavirussociety.org" abajo.
   Resolucion: implementado. Se agrego en footer y en la seccion Contact como contacto institucional ISH.

8. Requisito: incluir pestana "Former Meetings".
   Resolucion: implementado. Se creo la pagina `former-meetings/` con una experiencia editorial: bloque de lectureship awards, archivo historico por edicion, enlaces a abstract books disponibles y galeria visual recuperada desde el ZIP.

9. Requisito: incluir pestana "Communications".
   Resolucion: implementado. Se agrego la pestana y pagina `communications/` con Statement, WHO health topic, evento OMS Andes Virus MCM y webinar PHA4GE.

10. Requisito: Communications debe incluir Statement.
    Resolucion: implementado. Se agrego el PDF `Statement_ISH_Andes_v4.pdf` recuperado desde el ZIP y se dejo un resumen institucional en la pagina.

11. Requisito: Communications debe incluir News from WHO.
    Resolucion: implementado. Se agrego link a https://www.who.int/health-topics/hantavirus#tab=tab_1

12. Requisito: Communications debe incluir WHO meeting last week y notar que la Sociedad pudo moderar el primer bloque.
    Resolucion: implementado. Se agrego el evento OMS de 2026-05-15 y se indico que la Session 1 fue chaired by Nicole Tischler, segun agenda del evento revisada localmente.

13. Requisito: Communications debe incluir webinar PHA4GE sobre secuenciacion.
    Resolucion: implementado. Se agrego link a https://pha4ge.org/webinars/hantavirus-and-genomic-epidemiology-has-it-been-smooth-sailing/

14. Requisito: agregar proximo webinar OMS.
    Resolucion: implementado con fuente OMS disponible. Se agrego "Hantavirus in Focus I: what we know and what it means" del 20 de mayo de 2026 en Communications como noticia principal.

## Conference

15. Requisito: ICH2026 tiene un logo parecido y dos imagenes del lugar adjuntas.
    Resolucion: implementado. Se rescato desde `Webpage-20260519T141114Z-3-001.zip` la ilustracion `ICH2026_V4_landscape_recorte.png` y varias imagenes de Puerto Varas para el hero/galeria del congreso.

16. Requisito: primera pagina ICH2026 deberia incorporar el logo del meeting.
    Resolucion: implementado. Se incorporo la ilustracion/logo de meeting en el hero de ICH2026 como marca visual destacada.

17. Requisito: antes habia un carrusel para atractivos turisticos.
    Resolucion: implementado. Se agrego una galeria responsive con imagenes de Puerto Varas/Osorno/Lake District recuperadas desde el ZIP. La version actual evita scroll horizontal y muestra las imagenes como grilla adaptable.

18. Requisito: quitar o cambiar "Choose sessions", porque el meeting es chico.
    Resolucion: implementado. Se reemplazo por una ruta de informacion mas directa: Scientific Program ICH2026, ANDV Workshop, Keynote Speakers y Abstract Submission Registration.

19. Requisito: ordenar puntos 1-4 como Scientific Program ICH2026, ANDV Workshop, Keynote Speakers, Abstract Submission Registration.
    Resolucion: implementado en el bloque de ruta y en los modulos visuales principales de ICH2026.

20. Requisito: revisar si dejar las mismas fotos de los cuatro modulos.
    Resolucion: implementado. Se revisaron los assets disponibles del ZIP y no hay nuevas imagenes especificas para esos cuatro modulos. Se mantuvieron las imagenes generadas ya existentes porque son atingentes a Scientific Program ICH2026, ANDV Workshop, Keynote Speakers y Abstract Submission Registration. Si Nicole quiere otro enfoque visual, queda como decision editorial futura, no como bloqueo tecnico.

21. Requisito: Keynotes OK.
    Resolucion: sin cambios. La pagina se mantiene.

22. Requisito: Programme no deberia repetir la foto de la sociedad.
    Resolucion: implementado. Se cambio el hero de Programme a una imagen cientifica de hantavirus, no a la foto de archivo de la sociedad.

23. Requisito: Venue esta bien, pero algunos Travel resources deberian incorporarse mas arriba.
    Resolucion: implementado. Se agregaron accesos destacados a Survip Puerto Montt -> Puerto Varas y transfer SCL/Santiago dentro del primer bloque de Venue.

24. Requisito: el transfer email no se entiende que es en Santiago.
    Resolucion: implementado. Se renombraron y aclararon los recursos como Santiago/SCL transfer y se diferencio de Survip Puerto Montt -> Puerto Varas.

25. Requisito: faltan hoteles cerca del aeropuerto de Santiago.
    Resolucion: pendiente por insumo. Se agrego nota indicando que la lista de hoteles cerca de SCL sera incorporada cuando la organizacion la confirme.

26. Requisito: Sponsors deberia ser "Partners & Sponsors".
    Resolucion: implementado. Se actualizo la navegacion y pagina a Partners & Sponsors.

27. Requisito: sponsors actualizados estan en el poster enviado.
    Resolucion: implementado. Se uso `Poster ICH2026_v3.pdf` como fuente final, se extrajeron/recortaron logos visibles y se reorganizo la pagina en Sponsors, Scientific societies y Universities & research partners.

28. Requisito: el logo del header debe aparecer mas grande en el sitio web arriba porque identifica la sociedad.
    Resolucion: implementado. Se aumento el logo del header a 112px en desktop y 84px en mobile; el footer usa 116px para reforzar presencia institucional sin romper la navegacion.

29. Requisito: usar colores del poster para diferenciar mas Sociedad y Congreso.
    Resolucion: implementado. Se agrego una identidad visual especifica para paginas ICH2026 basada en `Poster ICH2026_v3.pdf`: azul ICH2026, celeste, teal y amarillo-lima como acento. Society mantiene un lenguaje institucional mas sobrio.

30. Requisito: revisar `Webpage-20260519T141114Z-3-001.zip` para assets faltantes, pero usar `Poster ICH2026_v3.pdf` como ultima version de poster.
    Resolucion: implementado. Se extrajeron desde el ZIP imagenes de Puerto Varas, Former Meetings, abstract books y el statement ISH Andes. No se uso ningun poster dentro del ZIP como referencia de colores/sponsors.

31. Requisito: Former Meetings debe ordenar el archivo completo I-XII con No., Year, Location, Abstract Book, Picture Galerie y Meeting Report.
    Resolucion: implementado. Se cargo la lista completa I-XII, con enlaces activos cuando hay PDF/imagen disponible y estados pendientes cuando falta meeting report o galeria.

32. Requisito: incluir texto de lectureship awards en Former Meetings.
    Resolucion: implementado. Se agrego un bloque editorial sobre Ho-Wang Lee Lifetime Achievement Award y Joel M. Dalrymple Memorial Award.

33. Requisito: usar imagenes del ZIP en Former Meetings y presentarlas con una experiencia premium, no solo una tabla.
    Resolucion: implementado. Se rescataron multiples imagenes de 2013 China, 2016 Colorado, 2019 Leuven y 2023 Seoul, y se creo una galeria visual por edicion con imagen principal, miniaturas y enlaces a abstract books.

34. Requisito: optimizar las imagenes nuevas usadas en el sitio.
    Resolucion: implementado. Se ejecuto `scripts/optimize_images.py`; el manifiesto ahora incluye variantes AVIF/WebP para las imagenes nuevas de ICH2026, Former Meetings y sponsors extraidos del poster.

35. Requisito: mover la referencia de la imagen viral a la esquina inferior derecha de la imagen referenciada y en letras blancas.
    Resolucion: implementado. El credito ahora se renderiza dentro del hero de About ISH como `page-hero-credit`, posicionado abajo a la derecha sobre la imagen y con texto blanco: "Image reference: CDC / Cynthia Goldsmith, 1993."

36. Requisito: eliminar en Partners & Sponsors la frase "Partners and sponsors were updated from Poster ICH2026_v3." y los subtitulos "Industry sponsors", "Scientific society partners" y "Universities, research centers and public agencies".
    Resolucion: implementado. Se reemplazo el texto del hero por una descripcion institucional y se dejaron los grupos solo como Sponsors, Scientific societies y Universities & research partners.

37. Requisito: eliminar en About ISH la frase "The society identity leads the institutional section, while ICH2026 remains a clearly separated conference area."
    Resolucion: implementado. Se removio esa bajada del bloque con logo institucional.

38. Requisito: mejorar la lectura estetica de ICH2026 Programme porque los colores del congreso dificultaban la lectura.
    Resolucion: implementado. La seccion de programa paso a una superficie clara con tarjetas blancas, texto oscuro y acentos del poster solo como lineas/badges. Se valido con Playwright en desktop y mobile.

39. Requisito: transformar Communications hacia una experiencia tipo noticias profesional y premium.
    Resolucion: implementado. Communications ahora usa formato newsroom no repetitivo: webinar OMS como noticia principal, panel editorial sin duplicar enlaces y grilla unica de recursos verificados. El Statement queda una sola vez como recurso principal.

40. Requisito: Former Meetings tenia encabezados repetitivos y las imagenes se abrian fuera de la pagina.
    Resolucion: implementado. Se reemplazaron los encabezados redundantes por "Conference record" y "Photo highlights", se mejoro la presentacion de las pocas fotos disponibles por edicion y se agrego lightbox interno para ampliar imagenes sin salir del sitio.

41. Requisito: validar que el sitio no tenga problemas tecnicos pendientes despues de los cambios.
    Resolucion: implementado. La validacion detecto cuatro imagenes alternativas del hero del homepage sin `width`/`height`; se agregaron dimensiones explicitas de 1855x848 en el generador para evitar saltos de layout y cumplir la validacion.

42. Requisito: en modo oscuro, la tabla de Conference record no era legible.
    Resolucion: implementado. Se agregaron estilos dark-mode especificos para `archive-table-wrap`, encabezados, celdas y links de fotos, con fondo azul oscuro y texto claro.

43. Requisito: borrar la frase "Each row keeps the core archive status clear: abstract book, available photographs and meeting-report material."
    Resolucion: implementado. Se elimino esa bajada del bloque Conference record en Former Meetings.

44. Requisito: todas las fotos deben poder verse en ambas secciones de Former Meetings.
    Resolucion: implementado. La tabla ahora lista todos los enlaces de fotos disponibles por edicion y la seccion de fotos mantiene imagen principal mas miniaturas, todas conectadas al lightbox interno.

45. Requisito: reemplazar "Not available yet" por "-" y quitar temporalmente Meeting Report.
    Resolucion: implementado. Los campos sin archivo ahora muestran "-" y la columna Meeting Report fue eliminada de la tabla hasta que exista material confirmado.

46. Requisito: simplificar "Photo highlights" y borrar la frase "The available photographs are presented as focused highlights rather than a separate external gallery."
    Resolucion: implementado. La seccion ahora se llama "Photos" y usa el titulo "Browse available meeting photos by edition.", sin texto explicativo adicional.

47. Requisito: en Communications eliminar el bloque "Editorial focus" con Institutional statements, WHO resources y Scientific webinars.
    Resolucion: implementado. Se elimino el panel editorial completo y la noticia principal queda como bloque unico.

48. Requisito: eliminar la frase "Each item links to a primary document, WHO page or scientific webinar, keeping the section concise and non-repetitive."
    Resolucion: implementado. Se borro esa bajada de Latest updates.

49. Requisito: dar mayor importancia visual al Statement de la sociedad, sin dejarlo mas largo.
    Resolucion: implementado. El Statement ahora usa una tarjeta destacada con fondo azul oscuro y texto claro, pero se removio el comportamiento que lo hacia ocupar mas alto que el resto.

50. Requisito: en ICH2026 quitar el scroll horizontal de la seccion de cuatro fotos de Puerto Varas.
    Resolucion: implementado. La galeria `location-carousel` paso de carrusel horizontal a grilla responsive de 4 columnas en desktop, 2 en tablet y 1 en mobile, sin overflow horizontal.

51. Requisito: en modo oscuro, la seccion "An excellent platform for students..." y sus modulos eran ilegibles.
    Resolucion: implementado. Se agregaron overrides dark-mode para ICH feature cards, titulos, textos y links, manteniendo el acento del congreso sobre superficies oscuras legibles.

52. Requisito: en modo oscuro, la seccion Programme con November 2-4 y November 5 era ilegible.
    Resolucion: implementado. Se corrigieron fondos, bordes y colores de texto de `program-track`, incluyendo el bloque destacado Andes Virus Workshop.

53. Requisito: en modo oscuro, Venue presentaba problemas de legibilidad.
    Resolucion: implementado. Se corrigieron fondos y colores de Venue, travel shortcuts, travel steps y travel detail list en modo oscuro.

54. Requisito: en modo oscuro, Partners & Sponsors presentaba problemas similares de legibilidad.
    Resolucion: implementado. Se corrigieron las tarjetas de sponsor en modo oscuro y se agrego fondo claro interno para logos, manteniendo texto legible.

## Homepage

55. Requisito: antes de continuar, generar una copia de la imagen actual del homepage.
    Resolucion: implementado. Se preservo una copia exacta de `assets/images/ui/home-science-hero.webp` en `assets/images/ui/home-science-hero.copia-20260521.webp`. Dimensiones: 1855x848. SHA256: `9b9d5931c2225e8b205841a059a7d4a094118c73153271f35e8a44d60a33fe3b`. Commit base al momento de la copia: `7c62d8a`.

56. Requisito: reemplazar la imagen activa del homepage por una version casi igual, con interior del emblema mas relleno, sin eliminar la antigua.
    Resolucion: implementado. `assets/images/ui/home-science-hero.webp` fue reemplazada por una version generada con el interior del emblema mas denso y volumetrico. La version anterior se conserva intacta en `assets/images/ui/home-science-hero.copia-20260521.webp`. Cache-bust activo: `filled-core-20260521`.

57. Requisito: corregir el relleno del emblema porque parecia un planeta y debe leerse como virus.
    Resolucion: implementado. Se reemplazo nuevamente `assets/images/ui/home-science-hero.webp` por una version con textura interior viral/microscopica, evitando lectura de planeta, crateres o superficie celeste. La copia anterior al proceso se mantiene en `assets/images/ui/home-science-hero.copia-20260521.webp`. Cache-bust activo: `virus-fill-20260521`.
