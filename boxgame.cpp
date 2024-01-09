#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>       

using namespace std;



int offer(const std::vector<int>& KalanKutular) {
    int sum = 0;
    for (int i : KalanKutular) {
        sum += i;
    }
    if (!KalanKutular.empty()) {
        int offer = sum / KalanKutular.size();
        return offer;
    } else {
        return 0;
    }
}



int main() {
    vector<int> KalanKutular = {100, 200, 300, 400, 500};
    vector<int> KarisikKutular;

    KarisikKutular = KalanKutular;
    unsigned seed = chrono::system_clock::now().time_since_epoch().count();
    shuffle(KarisikKutular.begin(), KarisikKutular.end(), default_random_engine(seed));
    for(int i = 0; i < KarisikKutular.size(); i++) {
        cout << "KarisikKutular[" << i << "] = " << KarisikKutular[i] << endl;
    }
    while (!KarisikKutular.empty()) {
        int choice;
        cout << "Select Box: ";
        cin >> choice;
        choice-=1;
        // Check if the choice is within the bounds of the vector
        if (choice >= 0 && choice < KarisikKutular.size()) {
            int secilenKutuSayi = KarisikKutular[choice];
            cout << "Selected money prıce " << secilenKutuSayi << endl;

            // Find the corresponding element in KalanKutular
            auto it = find(KalanKutular.begin(), KalanKutular.end(), KarisikKutular[choice]);
            if (it != KalanKutular.end()) {
                KalanKutular.erase(it);  // Remove the corresponding element from KalanKutular
            }
            KarisikKutular.erase(KarisikKutular.begin() + choice);  // Remove the element from KarisikKutular
        } else {
            cout << "Invalid index. Try again." << endl;
            continue;
        }

        // Print the remaining boxes in KalanKutular
        cout << "Remaining boxes in : ";
        if (KalanKutular.empty()){
            cout<<"your winning price "<<KalanKutular[0]<<endl;
            break;
        }
        for (int box : KalanKutular) {
            cout << box << " ";
        }
        cout << endl;
        int b;
        int a=offer(KalanKutular);
        cout<<"Offer for you from bank:"<<a<<endl;
        cout<<"If you want to except press 1 otherwise press 2:"<<endl;
        cin>>b;
        if(b==1){
            cout<<"Congrulastions you earned "<<a<<endl;
            break;
        }
        else{
            continue;
        }

    }


    return 0;
}