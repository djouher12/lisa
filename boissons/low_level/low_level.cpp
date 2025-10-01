#include <iostream>
#include <string>

class Localisation {

  string nom;
  int taxes;
  int prix_m2;

  Localisation(string a, int b, int c) : { nom(a), taxes(b), prix_m2(c) };
  void affichage() {
    cout << nom << ',' << taxes << " euros," << prix_m2 << " euros ." << endl;
  }
  ~Localisation();
};
