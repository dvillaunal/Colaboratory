{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Borrador_100DaysOfCode.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyM7kuE3HHdcIALoNahRWX9R",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/dvillaunal/Colaboratory/blob/main/Calculadora_MI.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UedqgylXPxHH"
      },
      "source": [
        "# EDAD:\n",
        "\n",
        "formato = \"%d/%m/%Y\"\n",
        "f_born = input('Fecha desde (dd/mm/aaaa): ')\n",
        "f_today = input('Fecha hasta (dd/mm/aaaa): ')\n",
        "\n",
        "if f_born == '' or f_today == '':\n",
        "    exit()\n",
        "\n",
        "try:                    \n",
        "    f_born = datetime.strptime(f_born, formato)\n",
        "    f_today = datetime.strptime(f_today, formato)    \n",
        "    if f_born < f_today:\n",
        "        print('Fecha de Nacimeinto debe ser menor o igual que Fecha Actual')\n",
        "\n",
        "        "
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}