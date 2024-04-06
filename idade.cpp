#include<iostream>
#include <string>
using namespace std;

int main(){
    string nome;
    float altura;
    int idade;

    cout << "digite o nome: " << endl;
    cin >> nome;
    cout << "\ndigite a altura: " << endl;
    cin >> altura;
    cout << "\ndigite a idade: " << endl;
    cin >> idade;

    cout << "O nome é: " << nome << endl;
    cout << "\nA altura é: " << altura << endl;
    cout << "\nA idade é: " << idade << endl;

    return 0;
}
