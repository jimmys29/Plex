# Core Pkgs
import streamlit as st
# EDA Pkgs
import pandas as pd
import codecs
import plotly as px
import altair as alt
from PIL import Image
# Components Pkgs
import streamlit.components.v1 as components
# Custome Component Fxn
import sweetviz as sv

st.set_page_config(
    page_title="DASHBOARD PLEX",
    page_icon="https://www.telefonica.com/documents/20195/146013668/telefonica-logo-azul.png/03c9a0c0-57eb-eb53-5649-79e382fd4965?t=1618483185177",
    layout="wide",
    initial_sidebar_state="expanded")

image = Image.open('TelefonicaL.jpg')
# rutimage = ""<img src="https://www.w3schools.com/howto/img_nature_wide.jpg" style="width:100%">""
# image= st.image("<img src=rutimage; style="width:100%">")
img = st.sidebar.image(image)


def st_display_sweetviz(report_html, width=1000, height=500):
    report_file = codecs.open(report_html, 'r')
    page = report_file.read()
    components.html(page, width=width, height=height, scrolling=True)


footer_temp = """

    <!-- CSS -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css" rel= 
                 "stylesheet"media="screen,projection"/>
    <link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity=
                "sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">


    <footer class="page-footer grey darken-4">
    <div class="container" id="aboutapp">
    <div class="row">
    <div class="col l6 s12">
    <h5 class="white-text">About Causacion Telefonica PlEx App</h5>
    <p class="grey-text text-lighten-4">Using Streamlit.</p>


    </div>

    <div class="col l3 s12">
    <h5 class="white-text">Connect With Me</h5>
    <ul>
    <a href=""https://www.telefonica.com/documents/20195/146016182/facebook-icon.png/752bd9ce-a2cf-8ccf-c906-ae9172935ea4?t=1619084036934"">
    <i class="fab fa-facebook fa-4x"></i>
    </a>
    <a href="https://www.linkedin.com/in/jaime-espindola-a5833447/" target="_blank" class="white-text">
    <i class="fab fa-linkedin fa-4x"></i>
    </a>
    <a href="https://www.telefonica.com/documents/20195/146016182/youtube-icon.png/8dd29ebe-b03d-dd41-7ccc-a30b51f95b76?t=1619084037794" target="_blank" class="white-text">
    <i class="fab fa-youtube-square fa-4x"></i>
    </a>
    <a href="https://www.telefonica.com/documents/20195/146016182/instagram-icon.png/51b9aca8-3e54-fe2e-4946-bed8501584b9?t=1619084037303" target="_blank" class="white-text">
    <i class="fab fa-github-square fa-4x"></i>
    </a>
    </ul>
    </div>
    </div>
    </div>
    <div class="footer-copyright">
    <div class="container">
    Made by, <a class="white-text text-lighten-3" href="https://www.telefonica.com/es/home"> Jaime Espindola</a><br/>
    <a class="white-text text-lighten-3" href="https://www.telefonica.com/es/home">@Jaime Espindola</a>
    </div>
    </div>
    </footer>
            """

html_temp = """
    <div style="background-color:royalblue;padding:1px;border-radius:1px">
    <h1 style="color:white;text-align:center;">DashBoard Causacion PlEx</h1>
    </div>
    """


# T1 = st.title("<h1 style='text-align: center;background:royalblue; color: white;'>Dash Board Causacion PlEx</h1>", "Dash")
def archivo():
    st.sidebar.title("Seleccione Archivo DashBoard")
    data_file = st.sidebar.file_uploader(" ", type=['xlsx'])
    return data_file


def main():
    """DASH BOARD TELEFONICA PLEX"""
    st.sidebar.title("<h4 style='text-align: right ;font-size=50; color: red;'>Seleccione archivo Origen</h4>", "File")
    data_file = st.sidebar.file_uploader(" ", type=['xlsx'])

    menu = ["Home", "Jefatura", "Anillo Antioquia", "Ftth", "Transformacion IP", "Banagrario", "About"]
    choice = st.sidebar.selectbox("Menu Proyectos", menu)

    st.title("<h4 style='text-align: right ;font-size=50; color: darkblue;'>Choise Proyect of Menu</h4>", "File")

    # OPCIONES A GRAFICAR
    tile_x = st.sidebar.selectbox(label="Seleccione Opcion  Eje_X",
                                    options=["PROYECTO", "SITIO", "GESTOR", "REGIONAL", "ID_PTO", "MES"],
                                    index=0)
    opcion = st.sidebar.radio("Seleccione Opcion  Eje_Y", ["COSTO", "CANTIDAD"])
    if not opcion:
        st.error("Por favor seleccione Una Opcion")

    def op( ):
        if opcion == "COSTO":
            opt = 'TOTAL'
        elif opcion == "CANTIDAD":
            opt = 'CANTIDAD'
            return opt

    tile_y = op()
    tile_col = st.sidebar.radio("Seleccione Opcion  Color", ["GRUPO", "CONTRATO", "EQUIPO", "PROYECTO"])
    if data_file is not None:
        dfup = pd.read_excel(data_file)
        # dfup = dfap[dfap['GRUPO'].dropna()]
        if choice == "Jefatura":
            st.subheader("Jefatura")
            # Selection para interaccion
            selector = alt.selection(type="single", empty='none')

            # Grafico General
            if st.checkbox('Ver Grafica Consolidado', menu):
                # st.line_chart(dfup)  # mostrar barra lateral
                Graf_Jef = alt.Chart(dfup).mark_boxplot(size=50, extent=3.0) \
                    .encode(x=alt.X(tile_x, title=tile_x),
                              y=alt.Y(tile_y, title=tile_y), color=tile_col, size='TIPO',
                              tooltip=['TIPO', 'TIPO', 'TOTAL', tile_y]).add_selection(
                    selector).interactive().properties(width=500, height=300)
                fig = px.histogram(dfup, x=tile_x, y=tile_y, color=tile_col,
                                     hover_data=['TIPO', 'ID_PTO', 'GESTOR'], labels={'TOTAL': 'TOTAL CAUSADO'})
                st.plotly_chart(fig)
                # Graf_Jef
                text = Graf_Jef.mark_text(align='left', baseline='middle', dx=3, font="Courier",
                                            fontSize=1).encode(text='TOTAL', size=alt.value(7))

                # fig = fig.add_trace(go.Funnel( dfup , x=tile_x , y=tile_y , color=tile_col ,
                # labels={'TOTAL': 'TOTAL CAUSADO'} )

                # st.plotly_chart ( fig )

            if st.checkbox('Mostrar Tabla de Datos'):
                st.write(dfup)
            if st.button("Generate Report"):
                # Normal Workflow
                report = sv.analyze(dfup)
                report.show_html()
                st_display_sweetviz("SWEETVIZ_REPORT.html")

        if choice == "Anillo Antioquia":
            st.subheader("Anillo Antioquia")
            dfpr = dfup[(dfup['PROYECTO'] == 'ANILLO ANTIOQUIA')]
            tot = dfup.groupby(['PROYECTO'])['PROYECTO', 'TOTAL'].sum()
            # Tot = dfup [ 'TOTAL' ].apply ( np.sum )
            # Selection para interaccion
            selector = alt.selection(type="single", empty='none')
            multi = alt.selection_multi()
            # Grafico General
            if st.checkbox('Ver Grafica Proyecto Anillo Antioquia', menu):
                # st.line_chart(data())  # mostrar barra lateral
                Graf_Proy = alt.Chart(dfpr).mark_bar(size=500 , cornerRadiusTopLeft=20) \
                    .encode ( x=alt.X(tile_x, title=tile_x),
                              y=alt.Y(tile_y, title=tile_y), color=tile_col, size='TIPO',
                              tooltip=['TIPO', 'TIPO', 'TOTAL', tile_y]) \
                    .add_selection(selector).interactive()

                # Graf_otr = alt.Chart ( dfpr ).transform_joinaggregate (TotalTOTAL='sum(TOTAL)' ,).transform_calculate(PercentOfTotal="datum.TOTAL / datum.TotalTOTAL").mark_bar().encode(alt.X('PercentOfTotal:Q', axis=alt.Axis(format='.0%')),y='GRUPO:N', color=tile_col)
                fig = px.histogram(dfpr, x=tile_x, y=tile_y, color=tile_col,
                                     hover_data=['TIPO', 'ID_PTO', 'GESTOR'], labels={'TOTAL': 'TOTAL CAUSADO'})
                st.plotly_chart(fig)
                text = Graf_Proy.mark_text(align='left', baseline='middle', dy=.1, font="Courier", fontSize=1,
                                             angle=270).encode(text='TOTAL', size=alt.value(7))
                # Graf_Proy

            if st.checkbox('Mostrar Tabla de Datos'):
                st.write(dfpr)
            if st.button("Generate Report"):
                # Normal Workflow
                report = sv.analyze(dfpr)
                report.show_html()
                st_display_sweetviz("SWEETVIZ_REPORT.html")

        dfup = pd.read_excel ( data_file )
        if choice == "Transformacion IP":
            st.subheader ( "Transformacion IP" )
            dfpr = dfup [ (dfup [ 'PROYECTO' ] == 'TRANSFORMACION IP') ]
            # Selection para interaccion
            selector = alt.selection ( type="single" , empty='none' )
            # Grafico General
            if st.checkbox ( 'Ver Grafica Proyecto' , menu ):
                # st.line_chart(data())  # mostrar barra lateral
                Graf_Proy = alt.Chart ( dfpr ).mark_bar ( size=50 ) \
                    .encode ( x=alt.X ( tile_x , title=tile_x ) ,
                              y=alt.Y ( tile_y , title=tile_y ) , color=tile_col , size='TIPO' ,
                              tooltip=[ 'TIPO' , 'TIPO' , 'TOTAL' , tile_y ] ) \
                    .add_selection ( selector ).interactive ()

                fig = px.histogram ( dfpr , x=tile_x , y=tile_y , color=tile_col , )
                st.plotly_chart ( fig )
                st.write ( Graf_Proy )
            if st.checkbox ( 'Mostrar Tabla de Datos' ):
                st.write ( dfpr )
            if st.button ( "Generate Report" ):
                # Normal Workflow
                report = sv.analyze ( dfpr )
                report.show_html ()
                st_display_sweetviz ( "SWEETVIZ_REPORT.html" )

        if choice == "Ftth":
            st.subheader ( "Ftth" )
            dfpr = dfup [ (dfup [ 'PROYECTO' ] == 'FTTH') ]

            # Selection para interaccion
            selector = alt.selection ( type="single" , empty='none' )
            # Grafico General
            if st.checkbox ( 'Ver Grafica Proyecto' , menu ):
                # st.line_chart(data())  # mostrar barra lateral
                Graf_Proy = alt.Chart ( dfpr ).mark_bar ( size=50 ) \
                    .encode ( x=alt.X ( tile_x , title=tile_x ) ,
                              y=alt.Y ( tile_y , title=tile_y ) , color=tile_col , size='TIPO' ,
                              tooltip=[ 'TIPO' , 'TIPO' , 'TOTAL' , tile_y ] ) \
                    .add_selection ( selector ).interactive ()

            fig = px.histogram ( dfpr , x=tile_x , y=tile_y , color=tile_col ,
                                 hover_data=[ 'TIPO' , 'ID_PTO' , 'GESTOR' ] , labels={'TOTAL': 'TOTAL CAUSADO'} )
            st.plotly_chart ( fig )
            # Graf_Proy
            if st.checkbox ( 'Mostrar Tabla de Datos' ):
                st.write ( dfpr )
            if st.button ( "Generate Report" ):
                # Normal Workflow
                report = sv.analyze ( dfpr )
                report.show_html ()
                st_display_sweetviz ( "SWEETVIZ_REPORT.html" )

        if choice == "Banagrario":
            st.subheader ( "Banagrario" )
            dfpr = dfup [ (dfup [ 'PROYECTO' ] == 'BANAGRARIO') ]
            # Selection para interaccion
            selector = alt.selection ( type="single" , empty='none' )
            # Grafico General
            if st.checkbox ( 'Ver Grafica Proyecto' , menu ):
                # st.line_chart(data())  # mostrar barra lateral
                Graf_Proy = alt.Chart ( dfpr ).mark_bar ( size=50 ) \
                    .encode ( x=alt.X ( tile_x , title=tile_x ) ,
                              y=alt.Y ( tile_y , title=tile_y ) , color=tile_col , size='TIPO' ,
                              tooltip=[ 'TIPO' , 'TIPO' , 'TOTAL' , tile_y ] ) \
                    .add_selection ( selector ).interactive ()
                fig = px.histogram ( dfpr , x=tile_x , y=tile_y , color=tile_col ,
                                     hover_data=[ 'TIPO' , 'ID_PTO' , 'GESTOR' ] , labels={'TOTAL': 'TOTAL CAUSADO'} )
                st.plotly_chart ( fig )
                # Graf_Proy
            if st.checkbox ( 'Mostrar Tabla de Datos' ):
                st.write ( dfpr )
            if st.button ( "Generate Report" ):
                # Normal Workflow
                report = sv.analyze ( dfpr )
                report.show_html ()
                st_display_sweetviz ( "SWEETVIZ_REPORT.html" )

        elif choice == "About":
            st.subheader ( "About DashBoard" )
            # components.iframe('https://telefonica.com')
            components.html ( footer_temp , height=500 )

    else:
        st.subheader ( "Home" )
        # components.html("<p style='color:red;'> Streamlit Components is Awesome</p>")
        components.html ( html_temp )

        components.html ( """ 
            <style>
            * {box-sizing: border-box}
            body {font-family: Verdana, sans-serif; margin:0}
            .mySlides {display: none}
            img {vertical-align: middle;}

            /* Slideshow container */
            .slideshow-container {
            max-width: 1000px;
            position: relative;
            margin: auto;
            }

            /* Next & previous buttons */
            .prev, .next {
            cursor: pointer;
            position: absolute;
            top: 50%;
            width: auto;
            padding: 16px;
            margin-top: -22px;
            color: white;
            font-weight: bold;
            font-size: 18px;
            transition: 0.6s ease;
            border-radius: 0 3px 3px 0;
            user-select: none;
            }

            /* Position the "next button" to the right */
            .next {
            right: 0;
            border-radius: 3px 0 0 3px;
            }

            /* On hover, add a black background color with a little bit see-through */
            .prev:hover, .next:hover {
            background-color: rgba(0,0,0,0.8);
            }

            /* Caption text */
            .text {
            color: #f2f2f2;
            font-size: 15px;
            padding: 8px 12px;
            position: absolute;
            bottom: 8px;
            width: 100%;
            text-align: center;
            }

            /* Number text (1/3 etc) */
            .numbertext {
            color: #f2f2f2;
            font-size: 12px;
            padding: 8px 12px;
            position: absolute;
            top: 0;
            }

            /* The dots/bullets/indicators */
            .dot {
            cursor: pointer;
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #bbb;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
            }

            .active, .dot:hover {
            background-color: #717171;
            }

            /* Fading animation */
            .fade {
            -webkit-animation-name: fade;
            -webkit-animation-duration: 1.5s;
            animation-name: fade;
            animation-duration: 1.5s;
            }

            @-webkit-keyframes fade {
            from {opacity: .4}
            to {opacity: 1}
            }

            @keyframes fade {
            from {opacity: .4}
            to {opacity: 1}
            }

            /* On smaller screens, decrease text size */
            @media only screen and (max-width: 300px) {
            .prev, .next,.text {font-size: 11px}
            }
            </style>
            </head>
            <body>

            <div class="slideshow-container">

            <div class="mySlides fade">
            <div class="numbertext">1 / 5</div>
            <img src="https://www.w3schools.com/howto/img_5terre_wide.jpg" style="width:100%">
            <div class="text">Caption Text</div>
            </div>
            
            <div class="mySlides fade">
            <div class="numbertext">2 / 5</div>
            <img src="https://www.w3schools.com/howto/img_nature_wide.jpg" style="width:100%">
            <div class="text">Caption Text</div>
            </div>

            <div class="mySlides fade">
            <div class="numbertext">3 / 5</div>
            <img src="https://www.w3schools.com/howto/img_snow_wide.jpg" style="width:100%">
            <div class="text">Caption Two</div>
            </div>

            <div class="mySlides fade">
            <div class="numbertext">4 / 5</div>
            <img src="https://www.w3schools.com/howto/img_mountains_wide.jpg" style="width:100%">
            <div class="text">Caption Three</div>
            </div>
                
            <div class="mySlides fade">
            <div class="numbertext">5 / 5</div>
            <img src="https://www.w3schools.com/howto/img_lights_wide.jpg" style="width:100%">
            <div class="text">Caption Three</div>
            </div>

            <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
            <a class="next" onclick="plusSlides(1)">&#10095;</a>

            </div>
            <br>

            <div style="text-align:center">
            <span class="dot" onclick="currentSlide(1)"></span>
            <span class="dot" onclick="currentSlide(2)"></span>
            <span class="dot" onclick="currentSlide(3)"></span>
            </div>

            <script>
            var slideIndex = 1;
            showSlides(slideIndex);

            function plusSlides(n) {
            showSlides(slideIndex += n);
            }

            function currentSlide(n) {
            showSlides(slideIndex = n);
            }

            function showSlides(n) {
            var i;
            var slides = document.getElementsByClassName("mySlides");
            var dots = document.getElementsByClassName("dot");
            if (n > slides.length) {slideIndex = 1}
            if (n < 1) {slideIndex = slides.length}
            for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
            }
            for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
            }
            slides[slideIndex-1].style.display = "block";
            dots[slideIndex-1].className += " active";
            }
            </script>
            """ )



if __name__ == '__main__':
    main ()
