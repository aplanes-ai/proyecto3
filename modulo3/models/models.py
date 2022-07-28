# -*- coding: utf-8 -*-
#Models.py

from wsgiref.handlers import format_date_time
from xmlrpc.client import Boolean
from odoo import models, fields, api

class Impresora(models.Model):
     _name = 'modulo3.impresora'
     _description = 'Listado de impresoras'

     name = fields.Char("Nombre" , required = True) #Nombre de la impresora
     image = fields.Image("Foto impresora") #Foto de la impresora
     impresora_tipo = fields.Many2one('modulo3.tipoimpresora', string='Tipo de impresora', required = True)
     impresora_pvp = fields.Float("P.V.P.", required = True) #Precio de venta al público
     impresora_precioproveedor = fields.Float("Precio proveedor", required = True) #Precio del proveedor
     impresora_codigo = fields.Char("Código", required = True) #Codigo de la impresora
     
     #Características técnicas principales
     impresora_resolucion = fields.Char(string = "Resolución de impresión")
     impresora_fcolor = fields.Boolean(string = "Impresión en color" , default = False)
     impresora_fwifi = fields.Boolean(string = "Conexión por WI-FI" , default = False)
     impresora_ftarjetared = fields.Boolean(string = "Tarjeta de Red" , default = False)
     impresora_fduplex = fields.Boolean(string = "Doble cara" , default = False)
     impresora_velocidad = fields.Float("Velocidad b/n (PPM)", required = True) #Velocidad de impresion en blanco y negro

     #Conectividad
     impresora_fbluetooth = fields.Boolean(string = "Conexión por Bluetooth" , default = False)
     impresora_puertosusb = fields.Integer(string = "Puertos USB" , default = False)

     #Escaneo
     impresora_fescaneo = fields.Boolean(string = "Función escaneo" , default = False)
     impresora_fescaneoformato = fields.Char("Formato")

     #Velocidad de impresión
      #impresion b/n = impresora_velocidad
     impresora_velocidadcolor = fields.Float("Velocidad color (PPM)") #Velocidad de impresion a color

     #Fax
     impresora_ffax = fields.Boolean(string = "Función Fax" , default = False)
     impresora_ffax1 = fields.Boolean(string = "Envío Fax a través de PC" , default = False)
     impresora_ffax2 = fields.Boolean(string = "Fax en color" , default = False)

     #Panel de control
     impresora_ftouchscreen = fields.Boolean(string = "Pantalla táctil" , default = False)
     impresora_ftouchscreencolor = fields.Boolean(string = "Pantalla táctil a color" , default = False)

     #Información ambiental
     impresora_ruidosidad = fields.Integer(string = "Decibelios de ruido")
     impresora_ruidosidad1 = fields.Boolean(string = "Certificación Energy Star" , default = False)
     impresora_ruidosidad2 = fields.Boolean(string = "Ecosostenible" , default = False)

     #Dimensiones y peso
     impresora_ancho = fields.Float("Ancho en cm")
     impresora_profundidad = fields.Float("Profundidad en cm")
     impresora_altura = fields.Float("Altura en cm")
     impresora_peso = fields.Float("Peso en Kg")

     #Incluido en paquete
     impresora_paquete_bateria = fields.Boolean(string = "Bateria" , default = False)
     impresora_paquete_cablered = fields.Boolean(string = "Cable de red" , default = False)
     impresora_paquete_cablealimentacion = fields.Boolean(string = "Cable de alimentación" , default = True)
     impresora_paquete_cableusb = fields.Boolean(string = "Cable USB" , default = False)
     impresora_paquete_cdsoftware = fields.Boolean(string = "CD Software" , default = False)

     #Consumo y energía de la impresora
     impresora_consumo_encendida = fields.Float(string = "Consumo de energía en W" , default = False)
     impresora_consumo_suspension = fields.Float(string = "Consumo en modo suspensión en W" , default = False)




     class TipoImpresora(models.Model):
          _name = 'modulo3.tipoimpresora'
          _description = 'Listado de tipos de impresoras'

          name = fields.Char("Tipo de impresora" , required = True) #Nombre del tipo de impresora