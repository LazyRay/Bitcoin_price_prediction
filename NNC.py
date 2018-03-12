import predict_btc_future
from sklearn import preprocessing
from sklearn.decomposition import IncrementalPCA
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
import pickle
from sklearn.externals import joblib

def runnnc():
    trade_data=predict_btc_future.get_agg_data()

    features=trade_data.drop(['next_price5','next_price10','next_price15'],axis=1)
    y1=trade_data['next_price5']
    y2=trade_data['next_price10']
    y3=trade_data['next_price15']
    PCA=IncrementalPCA(n_components=5)
    PCA.fit(features)
    PCA_feature=PCA.transform(features)
    
    X_train,X_test,y1_train,y1_test=train_test_split(PCA_feature,y1,test_size=0.33)
    nn=MLPClassifier()
    parameters={'activation':['identity','logistic','tanh','relu']}
    clf=GridSearchCV(nn,parameters)
    clf.fit(X_train,y1_train)

    X_train,X_test,y2_train,y2_test=train_test_split(PCA_feature,y2,test_size=0.33)
    nn=MLPClassifier()
    clf2=GridSearchCV(nn,parameters)
    clf2.fit(X_train,y2_train)

    X_train,X_test,y3_train,y3_test=train_test_split(PCA_feature,y3,test_size=0.33)
    nn=MLPClassifier()
    clf3=GridSearchCV(nn,parameters)
    clf3.fit(X_train,y3_train)
    
    joblib.dump(PCA,"pca.m")
    joblib.dump(clf,"next5.m")
    joblib.dump(clf2,"next10.m")
    joblib.dump(clf3,"next15.m")