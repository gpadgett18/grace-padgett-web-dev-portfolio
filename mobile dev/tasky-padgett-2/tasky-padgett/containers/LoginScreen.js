import React from 'react';
import { SafeAreaView, StyleSheet, View, Text, TextInput } from 'react-native';
import Header from '../components/Header';
import BlueButton from '../components/BlueButton';
// Required imports
//import React from 'react';
import { TouchableOpacity } from 'react-native';

export default class LoginScreen extends React.Component {
  state = {
    inputValue: '',
  }

  handleTextChange = (val) => {
    this.setState({ inputValue: val });
  }

  onButtonClicked = () => {
      if (this.state.inputValue) {
        console.log(this.state.inputValue)
        this.props.navigation.navigate('MainScreen')
      }
      else {
        alert('Enter a number');
      }
    }  
  
  render() {
    let { inputValue } = this.state;
    return (
      <SafeAreaView style={styles.container}>
        <Header instructions="Sign in to your account" />
        <Text style={styles.details}>
          Use your phone number to log into your account to view your tasks
        </Text>
        <View style={styles.form}>
          <Text style={styles.label}>Phone Number</Text>
          <TextInput 
            style={styles.input} 
            placeholder=""
            value={inputValue}
            keyboardType="number-pad" 
            onChangeText={this.handleTextChange}/>
          <BlueButton 
                style={{marginTop: 20 }} 
                title="Sign In" 
                onPress={this.onButtonClicked}
                />
        </View>
      </SafeAreaView>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#ffffff',
    flex: 1,
  },
  details: {
    color: '#2699FB',
    fontSize: 17,
    margin: 20,
  },
  form: {
    marginLeft: 20,
    marginRight: 20,
  },
  label: {
    fontSize: 12,
    color: '#2699FB',
    marginBottom: 5,
  },
  input: {
    backgroundColor: 'white',
    fontSize: 14,
    padding: 15,
    borderWidth: 1,
    borderColor: '#2699FB',
    borderStyle: 'solid',
  },
});
