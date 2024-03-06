import React from 'react';
import { View, Text, Image, ImageBackground, StyleSheet } from 'react-native';
import BlueButton from '../components/BlueButton';

const bgImage = require('../assets/paper.jpg');
const taskyIcon = require('../assets/tasky-logo.png');
const taskyLogo = require('../assets/tasky-name.png');

export default class SplashScreen extends React.Component {
    
    buttonHandler = () => {
      this.props.navigation.navigate('LoginScreen')
    }

    render() {
        return (
            <ImageBackground 
              source={bgImage} 
              style={styles.container}
            >
              <Image
                source={taskyIcon}
                style={styles.icon}
              />
              <Image
                source={taskyLogo}
                style={styles.logo}
                resizeMode="contain"
              />
              <Text style={styles.tagline}>GET THINGS DONE</Text>
              <BlueButton 
                title="GO" style={{ width: "100%" }} 
                onPress={this.buttonHandler}/>
            </ImageBackground>
        );
    }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingLeft: 25,
    paddingRight: 25,
    height: '100%',
  },
  icon: {
    width: 64,
    height: 64,
    marginBottom: 20,
  },
  logo: {
    width: 200,
    height: 50,
    marginBottom: 10,
  },
  tagline: {
    color: '#2699FB',
    textTransform: 'uppercase',
    textAlign: 'center',
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 50,
  },
});