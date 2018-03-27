void ReadLimitFromTree(TString filename){

  TFile *file = new TFile(filename);
  TTree *tree = (TTree *)file->Get("limit");

  double limit;
  tree->SetBranchAddress("limit",&limit);
  tree->GetEntry(0);
  cout << limit << endl;


}
