# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 23:11:23 2023

@author: Sergio Dominguez

"""
import pandas as pd
import numpy as np


def leer_tabla(tabla, engine):
    """
    Lee una tabla desde la base de datos y la carga en un DataFrame.

    Args:
        tabla (str): Nombre de la tabla a leer.
        engine: Objeto engine de la base de datos.

    Returns:
        pd.DataFrame: DataFrame que contiene los datos de la tabla.
    """
    
    return pd.read_sql(f"select * from {tabla}", engine)

def filtrar_dataframe_por_fechas(dataframe, columna_fecha, fecha_inicio, fecha_fin):
    
    """
    Filtra un DataFrame por un rango de fechas específico.

    Args:
        dataframe (pd.DataFrame): DataFrame a filtrar.
        columna_fecha (str): Nombre de la columna de fecha.
        fecha_inicio (str): Fecha de inicio del rango en formato 'YYYY-MM-DD'.
        fecha_fin (str): Fecha de fin del rango en formato 'YYYY-MM-DD'.

    Returns:
        pd.DataFrame: DataFrame filtrado.
    """
    
    dataframe[columna_fecha] = pd.to_datetime(dataframe[columna_fecha])
    
    return dataframe.query(f"orderDate >= '{fecha_inicio}' and orderDate <= '{fecha_fin}'")

def generar_reporte(dataframe, filas, columnas, valores, medida):
    
    """
    Genera un reporte pivotado a partir de un DataFrame.

    Args:
        dataframe (pd.DataFrame): DataFrame base.
        filas (str or list or None): Nombre(s) de la(s) columna(s) a utilizar como filas. Si filas es None, entonces columnas no puede ser None.
        columnas (str or list or None): Nombre(s) de la(s) columna(s) a utilizar como columnas. Si columnas es None, entonces filas no puede ser None.
        valores (str or list): Nombre(s) de la(s) columna(s) a utilizar como valores.
        medida (str or function): Función de agregación a aplicar a los valores.

    Returns:
        pd.DataFrame: DataFrame pivotado.
    """
    
    return pd.pivot_table(dataframe, 
                          index = filas, 
                          columns = columnas, 
                          values = valores, 
                          aggfunc = medida,
                          fill_value=0)

def guardar_tabla(dataframe, nombre_tabla, engine, if_exists = 'replace'):
    
    """
    Guarda un DataFrame en una tabla de la base de datos.

    Args:
        dataframe (pd.DataFrame): DataFrame a guardar.
        nombre_tabla (str): Nombre de la tabla.
        engine: Objeto engine de la base de datos.
        if_exists (str, optional): Comportamiento en caso de que la tabla exista. Por defecto, 'replace'.

    Returns:
        None
    """

    dataframe.to_sql(nombre_tabla, engine, index=False, if_exists = if_exists)
