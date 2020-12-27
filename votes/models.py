from django.db import models
from django.db.models import SET_NULL


class Department(models.Model):
    name = models.TextField(unique=True)


class Elections(models.Model):
    """Eg. Elecciones Generales 2021
    """
    name = models.TextField(unique=True)


class HojaVida(models.Model):
    election = models.ForeignKey(Elections, null=True, on_delete=SET_NULL)
    idHojaVida = models.IntegerField(null=True, blank=True, unique=True)


class Image(models.Model):
    image = models.TextField()


class Person(models.Model):
    dni_number = models.CharField(max_length=8, unique=True, null=True)
    first_names = models.TextField()
    last_names = models.TextField()
    elections = models.ManyToManyField(
        Elections,
        help_text="Elecciones donde postuló"
    )
    photo = models.ForeignKey(Image, null=True, on_delete=SET_NULL)

    idPersona = models.IntegerField(null=True, blank=True)
    intPosicion = models.IntegerField(null=True, blank=True)
    idCargoEleccion = models.IntegerField(null=True, blank=True)
    strCargoEleccion = models.TextField(null=True, blank=True)
    strDocumentoIdentidad = models.TextField(null=True, blank=True, unique=True)
    strApellidoPaterno = models.TextField(null=True, blank=True)
    strApellidoMaterno = models.TextField(null=True, blank=True)
    strNombres = models.TextField(null=True, blank=True)
    strFechaNacimiento = models.TextField(null=True, blank=True)
    strSexo = models.TextField(null=True, blank=True)
    intEstadosCandPer = models.IntegerField(null=True, blank=True)
    strEstado = models.TextField(null=True, blank=True)
    strNativo = models.TextField(null=True, blank=True)
    strJoven = models.TextField(null=True, blank=True)
    strDesignado = models.TextField(null=True, blank=True)
    idHojaVida = models.ForeignKey(HojaVida, null=True, blank=True, on_delete= models.SET_NULL)
    idOrganizacionPolitica = models.IntegerField(null=True, blank=True)
    idProcesoElectoral = models.IntegerField(null=True, blank=True)
    strProcesoElectoral = models.TextField(null=True, blank=True)
    strOrganizacionPolitica = models.TextField(null=True, blank=True)
    strAmbiente = models.TextField(null=True, blank=True)
    strAmbienteSije = models.TextField(null=True, blank=True)
    strUbigeoProcesal = models.TextField(null=True, blank=True)
    strDireccionProcesal = models.TextField(null=True, blank=True)
    strUbigeoDomicilio = models.TextField(null=True, blank=True)
    strDireccionDomicilio = models.TextField(null=True, blank=True)
    idJuradoElectoral = models.IntegerField(null=True, blank=True)
    idCandidatos = models.IntegerField(null=True, blank=True)
    idTipoEleccion = models.IntegerField(null=True, blank=True)
    strProvinciaConsejero = models.TextField(null=True, blank=True)
    idLista = models.IntegerField(null=True, blank=True)
    idCandidatoDeclara = models.IntegerField(null=True, blank=True)
    strUbigeoPostula = models.TextField(null=True, blank=True)
    intAlertas = models.IntegerField(null=True, blank=True)
    strCandidato = models.TextField(null=True, blank=True)
    strUbigeoPostulaDesc = models.TextField(null=True, blank=True)
    strDepartamento = models.TextField(null=True, blank=True)
    strProvincia = models.TextField(null=True, blank=True)
    strDistrito = models.TextField(null=True, blank=True)
    idAmbito = models.IntegerField(null=True, blank=True)
    strAmbito = models.TextField(null=True, blank=True)
    strCodExpedienteExt = models.TextField(null=True, blank=True)
    strAmbitoElectoral = models.TextField(null=True, blank=True)
    strCarneExtranjeria = models.TextField(null=True, blank=True)
    strPaisNacimiento = models.TextField(null=True, blank=True)
    strUbigeoNacimiento = models.TextField(null=True, blank=True)
    strNaciDepartamento = models.TextField(null=True, blank=True)
    strNaciProvincia = models.TextField(null=True, blank=True)
    strNaciDistrito = models.TextField(null=True, blank=True)
    strNaciUbiDepartamento = models.TextField(null=True, blank=True)
    strNaciUbiProvincia = models.TextField(null=True, blank=True)
    strNaciUbiDistrito = models.TextField(null=True, blank=True)
    strDomiDepartamento = models.TextField(null=True, blank=True)
    strDomiProvincia = models.TextField(null=True, blank=True)
    strDomiDistrito = models.TextField(null=True, blank=True)
    strDomiUbiDepartamento = models.TextField(null=True, blank=True)
    strDomiUbiProvincia = models.TextField(null=True, blank=True)
    strDomiUbiDistrito = models.TextField(null=True, blank=True)
    strDomicilioDirecc = models.TextField(null=True, blank=True)
    strPostulaDepartamento = models.TextField(null=True, blank=True)
    strPostulaProvincia = models.TextField(null=True, blank=True)
    strPostulaDistrito = models.TextField(null=True, blank=True)
    strPostulaUbiDepartamento = models.TextField(null=True, blank=True)
    strPostulaUbiProvincia = models.TextField(null=True, blank=True)
    strPostulaUbiDistrito = models.TextField(null=True, blank=True)
    strAnioPostula = models.TextField(null=True, blank=True)
    strterminoregistro = models.TextField(null=True, blank=True)
    idCandidato = models.IntegerField(null=True, blank=True)
    strRegistro = models.TextField(null=True, blank=True)
    idEstado = models.IntegerField(null=True, blank=True)
    strUsuario = models.TextField(null=True, blank=True)
    strRutaArchivo = models.TextField(null=True, blank=True)
    decPorcentaje = models.IntegerField(null=True, blank=True)
    strNombreArchivo = models.TextField(null=True, blank=True)
    idParamHojaVida = models.IntegerField(null=True, blank=True)
    strHojaVida = models.TextField(null=True, blank=True)
    strFeTerminoRegistro = models.TextField(null=True, blank=True)
    strEnlaceMenu = models.TextField(null=True, blank=True)
    strClase = models.TextField(null=True, blank=True)
    idUsuario = models.IntegerField(null=True, blank=True)
    intPagina = models.IntegerField(null=True, blank=True)
    intCantidadPagina = models.IntegerField(null=True, blank=True)
    intCantidadReg = models.IntegerField(null=True, blank=True)
    intItem = models.IntegerField(null=True, blank=True)
    strEstadoLocal = models.TextField(null=True, blank=True)
    strIdOrgPolitica = models.TextField(null=True, blank=True)
    idEstadoCandidato = models.TextField(null=True, blank=True)
    intVotoPreferencial = models.IntegerField(null=True, blank=True)
    strDistritoElectoral = models.TextField(null=True, blank=True)
    strIdDistritoElectoral = models.TextField(null=True, blank=True)
    intTotalPersonero = models.IntegerField(null=True, blank=True)
    intOrden = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ['first_names', 'last_names']

    def __str__(self):
        return f'{self.last_names}, {self.first_names} (DNI: {self.dni_number})'


class Ingresos(models.Model):
    election = models.ForeignKey(Elections, null=True, on_delete=SET_NULL)
    person = models.ForeignKey(Person, null=True, on_delete=SET_NULL)
    idHojaVida = models.ForeignKey(HojaVida, null=True, blank=True, on_delete= models.SET_NULL)
    idHVIngresos = models.IntegerField(null=True, blank=True, unique=True)
    idEstado = models.IntegerField(null=True, blank=True)
    decRemuBrutaPublico = models.IntegerField(null=True, blank=True)
    decRemuBrutaPrivado = models.IntegerField(null=True, blank=True)
    decRentaIndividualPublico = models.IntegerField(null=True, blank=True)
    decRentaIndividualPrivado = models.IntegerField(null=True, blank=True)
    decOtroIngresoPublico = models.IntegerField(null=True, blank=True)
    decOtroIngresoPrivado = models.IntegerField(null=True, blank=True)
    strUsuario = models.TextField(null=True, blank=True)
    strTengoIngresos = models.TextField(null=True, blank=True)
    strAnioIngresos = models.TextField(null=True, blank=True)


class SentenciaObliga(models.Model):
    election = models.ForeignKey(Elections, null=True, on_delete=SET_NULL)
    person = models.ForeignKey(Person, null=True, on_delete=SET_NULL)
    idHVSentenciaObliga = models.IntegerField(null=True, blank=True, unique=True)
    idHojaVida = models.ForeignKey(HojaVida, null=True, blank=True, on_delete= models.SET_NULL)
    intItemSentenciaObliga = models.IntegerField(null=True, blank=True)
    idEstado = models.IntegerField(null=True, blank=True)
    idParamMateriaSentencia = models.IntegerField(null=True, blank=True)
    strTengoSentenciaObliga = models.TextField(null=True, blank=True)
    strMateriaSentencia = models.TextField(null=True, blank=True)
    strExpedienteObliga = models.TextField(null=True, blank=True)
    strOrganoJuridicialObliga = models.TextField(null=True, blank=True)
    strFalloObliga = models.TextField(null=True, blank=True)
    strEstado = models.TextField(null=True, blank=True)
    strUsuario = models.TextField(null=True, blank=True)
    strOrder = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.strMateriaSentencia} {self.strFalloObliga}"


class EduUniversitaria(models.Model):
    election = models.ForeignKey(Elections, null=True, on_delete=SET_NULL)
    person = models.ForeignKey(Person, null=True, on_delete=SET_NULL)
    idHVEduUniversitaria = models.IntegerField(null=True, blank=True, unique=True)
    idHojaVida = models.ForeignKey(HojaVida, null=True, blank=True, on_delete= models.SET_NULL)
    intItemEduUni = models.IntegerField(null=True, blank=True)
    idEstado = models.IntegerField(null=True, blank=True)
    strTengoEduUniversitaria = models.TextField(null=True, blank=True)
    strEduUniversitaria = models.TextField(null=True, blank=True)
    strUniversidad = models.TextField(null=True, blank=True)
    strCarreraUni = models.TextField(null=True, blank=True)
    strConcluidoEduUni = models.TextField(null=True, blank=True)
    strEgresadoEduUni = models.TextField(null=True, blank=True)
    strBachillerEduUni = models.TextField(null=True, blank=True)
    strAnioBachiller = models.TextField(null=True, blank=True)
    strTituloUni = models.TextField(null=True, blank=True)
    strAnioTitulo = models.TextField(null=True, blank=True)
    strUsuario = models.TextField(null=True, blank=True)
    strMetodoAccion = models.TextField(null=True, blank=True)
    strOrder = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.idHojaVida.id} {self.strUniversidad} {self.strCarreraUni}"


class EduBasica(models.Model):
    election = models.ForeignKey(Elections, null=True, on_delete=SET_NULL)
    person = models.ForeignKey(Person, null=True, on_delete=SET_NULL)
    idHVEduBasica = models.IntegerField(null=True, blank=True, unique=True)
    idHojaVida = models.ForeignKey(HojaVida, null=True, blank=True, on_delete= models.SET_NULL)
    idEstado = models.IntegerField(null=True, blank=True)
    strTengoEduBasica = models.TextField(null=True, blank=True)
    strEduPrimaria = models.TextField(null=True, blank=True)
    strConcluidoEduPrimaria = models.TextField(null=True, blank=True)
    strEduSecundaria = models.TextField(null=True, blank=True)
    strConcluidoEduSecundaria = models.TextField(null=True, blank=True)
    strUsuario = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.idHojaVida.id}"


class EduNoUniversitaria(models.Model):
    election = models.ForeignKey(Elections, null=True, on_delete=SET_NULL)
    person = models.ForeignKey(Person, null=True, on_delete=SET_NULL)
    idHVNoUniversitaria = models.IntegerField(null=True, blank=True, unique=True)
    idHojaVida = models.ForeignKey(HojaVida, null=True, blank=True, on_delete= models.SET_NULL)
    idEstado = models.IntegerField(null=True, blank=True)
    strTengoNoUniversitaria = models.TextField(null=True, blank=True)
    strEduNoUniversitaria = models.TextField(null=True, blank=True)
    strCentroEstudioNoUni = models.TextField(null=True, blank=True)
    strCarreraNoUni = models.TextField(null=True, blank=True)
    strConcluidoNoUni = models.TextField(null=True, blank=True)
    strUsuario = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.idHojaVida.id} {self.strCentroEstudioNoUni}"


class EduTecnica(models.Model):
    election = models.ForeignKey(Elections, null=True, on_delete=SET_NULL)
    person = models.ForeignKey(Person, null=True, on_delete=SET_NULL)
    idHVEduTecnico = models.IntegerField(null=True, blank=True, unique=True)
    idHojaVida = models.ForeignKey(HojaVida, null=True, blank=True, on_delete= models.SET_NULL)
    idEstado = models.IntegerField(null=True, blank=True)
    strTengoEduTecnico = models.TextField(null=True, blank=True)
    strCenEstudioTecnico = models.TextField(null=True, blank=True)
    strCarreraTecnico = models.TextField(null=True, blank=True)
    strConcluidoEduTecnico = models.TextField(null=True, blank=True)
    strUsuario = models.TextField(null=True, blank=True)


class InfoAdicional(models.Model):
    election = models.ForeignKey(Elections, null=True, on_delete=SET_NULL)
    person = models.ForeignKey(Person, null=True, on_delete=SET_NULL)
    idHVInfoAdicional = models.IntegerField(null=True, blank=True, unique=True)
    idHojaVida = models.ForeignKey(HojaVida, null=True, blank=True, on_delete= models.SET_NULL)
    idEstado = models.IntegerField(null=True, blank=True)
    strTengoInfoAdicional = models.TextField(null=True, blank=True)
    strInfoAdicional = models.TextField(null=True, blank=True)
    strUsuario = models.TextField(null=True, blank=True)


class Anotacion(models.Model):
    election = models.ForeignKey(Elections, null=True, on_delete=SET_NULL)
    person = models.ForeignKey(Person, null=True, on_delete=SET_NULL)
    idAnotacionMarginal = models.IntegerField(null=True, blank=True, unique=True)
    idHojaVida = models.ForeignKey(HojaVida, null=True, blank=True, on_delete= models.SET_NULL)
    idEstado = models.IntegerField(null=True, blank=True)
    idEstadoAnotacion = models.IntegerField(null=True, blank=True)
    idCargoEleccion = models.IntegerField(null=True, blank=True)
    idProcesoElectoral = models.IntegerField(null=True, blank=True)
    idOrganizacionPolitica = models.IntegerField(null=True, blank=True)
    idJuradoElectoral = models.IntegerField(null=True, blank=True)
    idTipoAnotacion = models.IntegerField(null=True, blank=True)
    idSeccionHV = models.IntegerField(null=True, blank=True)
    strNroAnotacion = models.TextField(null=True, blank=True)
    strFeAnotacion = models.TextField(null=True, blank=True)
    strNroExpediente = models.TextField(null=True, blank=True)
    strNroInforme = models.TextField(null=True, blank=True)
    strNroDocumento = models.TextField(null=True, blank=True)
    strDocumentoIdentidad = models.TextField(null=True, blank=True)
    strApellidoPaterno = models.TextField(null=True, blank=True)
    strApellidoMaterno = models.TextField(null=True, blank=True)
    strNombres = models.TextField(null=True, blank=True)
    strCandidato = models.TextField(null=True, blank=True)
    strCargoEleccion = models.TextField(null=True, blank=True)
    strTipoAnotacion = models.TextField(null=True, blank=True)
    strSeccionHV = models.TextField(null=True, blank=True)
    strDice = models.TextField(null=True, blank=True)
    strDebeDecir = models.TextField(null=True, blank=True)
    strOrganizacionPolitica = models.TextField(null=True, blank=True)
    strProcesoElectoral = models.TextField(null=True, blank=True)
    strEstado = models.TextField(null=True, blank=True)
    strUsuario = models.TextField(null=True, blank=True)
    strUsuarioAprueba = models.TextField(null=True, blank=True)
    FGSeleccionado = models.TextField(null=True, blank=True)


class EduPosgrado(models.Model):
    election = models.ForeignKey(Elections, null=True, on_delete=SET_NULL)
    person = models.ForeignKey(Person, null=True, on_delete=SET_NULL)
    idHVPosgrado = models.IntegerField(null=True, blank=True, unique=True)
    idHojaVida = models.ForeignKey(HojaVida, null=True, blank=True, on_delete= models.SET_NULL)
    idEstado = models.IntegerField(null=True, blank=True)
    intItemPosgrado = models.IntegerField(null=True, blank=True)
    strTengoPosgrado = models.TextField(null=True, blank=True)
    strCenEstudioPosgrado = models.TextField(null=True, blank=True)
    strEspecialidadPosgrado = models.TextField(null=True, blank=True)
    strConcluidoPosgrado = models.TextField(null=True, blank=True)
    strEgresadoPosgrado = models.TextField(null=True, blank=True)
    strEsMaestro = models.TextField(null=True, blank=True)
    strEsDoctor = models.TextField(null=True, blank=True)
    strAnioPosgrado = models.TextField(null=True, blank=True)
    strUsuario = models.TextField(null=True, blank=True)


class SentenciaPenal(models.Model):
    election = models.ForeignKey(Elections, null=True, on_delete=SET_NULL)
    person = models.ForeignKey(Person, null=True, on_delete=SET_NULL)
    idHVSentenciaPenal = models.IntegerField(null=True, blank=True, unique=True)
    idHojaVida = models.ForeignKey(HojaVida, null=True, blank=True, on_delete= models.SET_NULL)
    intItemSentenciaPenal = models.IntegerField(null=True, blank=True)
    idParamModalidad = models.IntegerField(null=True, blank=True)
    idParamCumpleFallo = models.IntegerField(null=True, blank=True)
    idEstado = models.IntegerField(null=True, blank=True)
    strTengoSentenciaPenal = models.TextField(null=True, blank=True)
    strExpedientePenal = models.TextField(null=True, blank=True)
    strFechaSentenciaPenal = models.TextField(null=True, blank=True)
    strOrganoJudiPenal = models.TextField(null=True, blank=True)
    strDelitoPenal = models.TextField(null=True, blank=True)
    strFalloPenal = models.TextField(null=True, blank=True)
    strModalidad = models.TextField(null=True, blank=True)
    strOtraModalidad = models.TextField(null=True, blank=True)
    strCumpleFallo = models.TextField(null=True, blank=True)
    strUsuario = models.TextField(null=True, blank=True)
    strOrder = models.TextField(null=True, blank=True)


class BienMuebleOtro(models.Model):
    election = models.ForeignKey(Elections, null=True, on_delete=SET_NULL)
    person = models.ForeignKey(Person, null=True, on_delete=SET_NULL)
    idHojaVida = models.ForeignKey(HojaVida, null=True, blank=True, on_delete= models.SET_NULL)
    idHVMuebleOtro = models.IntegerField(null=True, blank=True, unique=True)
    intItemMuebleOtro = models.IntegerField(null=True, blank=True)
    idEstado = models.IntegerField(null=True, blank=True)
    decValor = models.IntegerField(null=True, blank=True)
    strTengoBienMuebleOtro = models.TextField(null=True, blank=True)
    strOtroBien = models.TextField(null=True, blank=True)
    strDescripcion = models.TextField(null=True, blank=True)
    strCaracteristica = models.TextField(null=True, blank=True)
    strUsuario = models.TextField(null=True, blank=True)
    strOrder = models.TextField(null=True, blank=True)


class BienMueble(models.Model):
    election = models.ForeignKey(Elections, null=True, on_delete=SET_NULL)
    person = models.ForeignKey(Person, null=True, on_delete=SET_NULL)
    idHojaVida = models.ForeignKey(HojaVida, null=True, blank=True, on_delete= models.SET_NULL)
    idHVBienMueble = models.IntegerField(null=True, blank=True, unique=True)
    intItemMueble = models.IntegerField(null=True, blank=True)
    idEstado = models.IntegerField(null=True, blank=True)
    decValor = models.IntegerField(null=True, blank=True)
    strTengoBienMueble = models.TextField(null=True, blank=True)
    strVehiculo = models.TextField(null=True, blank=True)
    strMarca = models.TextField(null=True, blank=True)
    strPlaca = models.TextField(null=True, blank=True)
    strUsuario = models.TextField(null=True, blank=True)
    strModelo = models.TextField(null=True, blank=True)
    strAnio = models.TextField(null=True, blank=True)
    strCaracteristica = models.TextField(null=True, blank=True)
    strOrder = models.TextField(null=True, blank=True)
    strComentario = models.TextField(null=True, blank=True)


class BienInmueble(models.Model):
    election = models.ForeignKey(Elections, null=True, on_delete=SET_NULL)
    person = models.ForeignKey(Person, null=True, on_delete=SET_NULL)
    idHVBienInmueble = models.IntegerField(null=True, blank=True, unique=True)
    idHojaVida = models.ForeignKey(HojaVida, null=True, blank=True, on_delete= models.SET_NULL)
    intItemInmueble = models.IntegerField(null=True, blank=True)
    decAutovaluo = models.IntegerField(null=True, blank=True)
    idEstado = models.IntegerField(null=True, blank=True)
    decUIT = models.IntegerField(null=True, blank=True)
    strTengoInmueble = models.TextField(null=True, blank=True)
    strTipoBienInmueble = models.TextField(null=True, blank=True)
    strUbigeoInmueble = models.TextField(null=True, blank=True)
    strInmuebleUbiDepartamento = models.TextField(null=True, blank=True)
    strInmuebleUbiProvincia = models.TextField(null=True, blank=True)
    strInmuebleUbiDistrito = models.TextField(null=True, blank=True)
    strInmueblePais = models.TextField(null=True, blank=True)
    strInmuebleDepartamento = models.TextField(null=True, blank=True)
    strInmuebleProvincia = models.TextField(null=True, blank=True)
    strInmuebleDistrito = models.TextField(null=True, blank=True)
    strInmuebleDireccion = models.TextField(null=True, blank=True)
    strInmuebleSunarp = models.TextField(null=True, blank=True)
    strPartidaSunarp = models.TextField(null=True, blank=True)
    strFichaTomoSunarp = models.TextField(null=True, blank=True)
    strUsuario = models.TextField(null=True, blank=True)
    strOrder = models.TextField(null=True, blank=True)
    strComentario = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.strTipoBienInmueble} S/. {self.decAutovaluo}"


class Expediente(models.Model):
    election = models.ForeignKey(Elections, null=True, on_delete=SET_NULL)
    person = models.ForeignKey(Person, null=True, on_delete=SET_NULL)
    id_expediente = models.IntegerField(null=True, blank=True)
    str_cod_expediente_ext = models.TextField(null=True, blank=True)
    str_cod_expediente = models.TextField(null=True, blank=True)
    id_organizacion_politica = models.IntegerField(null=True, blank=True)
    str_organizacion_politica = models.TextField(null=True, blank=True)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete= models.SET_NULL)
    str_provincia = models.TextField(null=True, blank=True)
    str_distrito = models.TextField(null=True, blank=True)
    str_estado_exped = models.TextField(null=True, blank=True)
    str_tipo_eleccion = models.TextField(null=True, blank=True)
    id_jurado_electoral = models.IntegerField(null=True, blank=True)
    str_jurado_electoral = models.TextField(null=True, blank=True)
    id_tipo_expediente = models.IntegerField(null=True, blank=True)
    str_tipo_expediente = models.TextField(null=True, blank=True)
    id_materia = models.IntegerField(null=True, blank=True)
    str_materia = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.str_organizacion_politica} - {self.department.name}"


class Vote(models.Model):
    # can be SI, NO, aust. awe. etc
    name = models.CharField(max_length=100, unique=True)


class Legislature(models.Model):
    name = models.TextField(unique=True)


class ProjectLaw(models.Model):
    # proyecto de ley
    number_short = models.IntegerField()


class VoteEvent(models.Model):
    # store each voting event for each congress person
    # Mauricio Mulder vote SI for projects number 10 and 20 on date and for
    # such legislature
    legislature = models.ForeignKey(Legislature, null=True, on_delete=SET_NULL)
    vote_date = models.DateTimeField()
    vote_projects = models.ManyToManyField(ProjectLaw)
    person = models.ForeignKey(Person, null=True, on_delete=SET_NULL)
    vote = models.ForeignKey(Vote, null=True, on_delete=SET_NULL)
