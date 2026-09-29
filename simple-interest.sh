#!/bin/bash
# Script para calcular el interés simple

# Solicitar datos al usuario
read -p "Ingrese el capital (P): " P
read -p "Ingrese la tasa de interés anual (R): " R
read -p "Ingrese el tiempo en años (T): " T

# Validar entradas
if [[ -z "$P" || -z "$R" || -z "$T" ]]; then
  echo "Error: Todos los campos son obligatorios."
  exit 1
fi

# Calcular interés simple
SI=$(echo "$P * $R * $T / 100" | bc -l)

# Calcular monto total
A=$(echo "$P + $SI" | bc -l)

# Mostrar resultados
echo "Interés Simple: $SI"
echo "Monto Total: $A"

