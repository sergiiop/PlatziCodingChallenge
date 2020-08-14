package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Convertir horas y minutos a segundos")
	fmt.Println("Ingresa las horas y los minutos a convertir.")
	fmt.Println("Dividelos entre si con un espacio EJ: (3 40)")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	horasMinutos := scanner.Text()
	valores := strings.Split(horasMinutos, " ")
	horas, _ := strconv.Atoi(valores[0])
	minutos, _ := strconv.Atoi(valores[1])
	segundos := (horas * 3600) + (minutos * 60)
	fmt.Println(horas, "hrs y ", minutos, " minutos, equivalen a: ", segundos, " segundos")
}
