from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression

def build_and_train_model(data):
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(data)
    X, y = [], []
    for i in range(len(scaled) - 1):
        X.append(scaled[i])
        y.append(scaled[i + 1])
    model = LinearRegression().fit(X, y)
    return model, scaler
