package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Calcula el area de un triangulo")
	fmt.Println("Ingresa la base y la altura del triangulo en ese orden EJ:9 3")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	operacion := scanner.Text()
	valores := strings.Split(operacion, " ")
	base, _ := strconv.Atoi(valores[0])
	altura, _ := strconv.Atoi(valores[1])
	fmt.Println("La base es ", base)
	fmt.Println("La altura es ", altura)
	area := (base * altura) / 2
	fmt.Println("El area total del triangulo es ", area)
	if base < altura {
		fmt.Println("El triangulo es isósceles")
	}
	if base > altura {
		fmt.Println("El triangulo es escaleno")
	} else {
		fmt.Println("El triangulo es equilátero")
	}
}
