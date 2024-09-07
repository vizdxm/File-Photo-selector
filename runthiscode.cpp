#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
string heading,ending;

void print(string ID,string destination) {
  cout << "copy " << heading << ID << ending << " " << destination << " \n";
}

string tostring(int x) {
  string r = "0000";
  r[0] = x/1000 + '0';
  x%=1000;
  r[1] = x/100 + '0';
  x%=100;
  r[2] = x/10 + '0';
  x%=10;
  r[3] = x + '0';
  return r;
}

int main () {
  vector <string> id; //id.push_back("dummy");
  string des;
  cout << "user manual:\n1. Open command prompt and select original file folder by typing 'cd' and the path to the folder\n2. Create a folder that will be the destination for the selected files in the original folder\n3. Then enter the desination folder name and the file IDs ending with a 0 in this program. \n4. Finally copy the output of this program to paste in the command prompt, enter and just wait for the files to be copied to the destination folder.\nnote : this program alse removes duplicate IDs and sorts the IDs in ascending order.\n\n";
  cout << "Ex: selecting wedding photo number 2 89 40 and 600 for editing\n(in CMD prompt) cd C:\\documents\\photos\\wedding_photos\n(in wedding_photos folder) create new folder -  for_editing\n(run this code and enter) canonR6___, .jpg, for_editing, 2 89 40 600 0\n(in CMD prompt) paste the text generated from this code and done\n\n\n";
  
  cout << "enter file heading (ex: CanonR6__) : ";
  cin >> heading;
  cout << "enter file ending (ex: .jpg) : ";
  cin >> ending;
  cout << "enter destination folder name : ";
  cin >> des;
  
  cout << "enter photo id list, ending with 0 : ";
  while(true) {
  	int a; cin >> a;
  	if(a==0)
  		break;
    id.push_back(tostring(a));
  }
  sort(id.begin(),id.end());
  id.insert(id.begin(),"dummy");
  cout << "\nCOPY BELOW\n\n";

  for(int i=0;i<id.size();i++)
    if(i!=0 && id[i]!=id[i-1])
      print(id[i],des);
  return 0;
}
