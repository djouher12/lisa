#include <cpr/cpr.h>
#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>
#include <string>

using namespace std;

class Localisation {
public:
  string nom;
  int taxes;
  int prix_m2;
  int id;

  Localisation(string a, int b, int c) : nom(a), taxes(b), prix_m2(c) {};
  Localisation(data.nom, data.taxes, data.prix_m2) {};
  Localisation(int x) : id(x) {};
  void affichage() {
    cout << nom << ',' << taxes << " euros," << prix_m2 << " euros ." << endl;
  }
  //~Localisation();
};
using json = nlohmann::json;
int main() {
  Localisation localisation1("Paris", 50, 6000);
  cout << localisation1.nom << endl;

  cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/local/1"});

  r.status_code;            // 200
  r.header["content-type"]; // application/json; charset=utf-8
  cout << r.text;
  // JSON text string

  json data = json::parse(r.text);
  Localisation localisation2(data.nom, data.taxes, data.prix_m2);
  return 0;
}
