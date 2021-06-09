#include <iostream>
#include <nlohmann/json.hpp>
#include <string>
#include <fstream>

using json = nlohmann::json;
using namespace std;




int main()
{
    json j;
    ofstream fout;
    char a, b;
    bool retry;
    setlocale(LC_ALL, "ru");


    cout << "Приветствую в редакторе библиотек AnyLang\n *Введите слово а затем его перевод и нажмите кнопку ввода\n *Когда решите начать - введите go\n *Когда решите закончить библиотеку - введите 'esc' \n";
    string str{};
    cin >> str;

    if (str[0] == 'g' && str[1] == 'o') {
        do {
            retry = false;
            for (int c = 1; c == c; c++) {
                string s1;
                string s2;
                cout << "=======================================================================\nВведите " << c << " слово\n";
                cin >> s1;
                if (s1[0] == 'e' && s1[1] == 's' && s1[2] == 'c') {
                    j["any"] =  u8"Любой";
                    fout.open ("dict.json");
                    fout << j;
                    fout.close();
                    retry == true;
                    break;
                }
                else {
                    cout << "Введите перевод слова " << s1 << "\n";
                    cin >> s2;
                    j[s1] = s2;
                    
                }

            }
        } while (retry);
        cout << "Прощайте!";
    }
    else {
        cout << "Вы не ввели 'go' тем самым завершив работу приложения";
    }
}