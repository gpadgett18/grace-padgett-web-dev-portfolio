import React from 'react';
import { View, Text, Image, StyleSheet } from 'react-native';

const taskyIcon = require('../assets/tasky-logo.png');

export default class Header extends React.Component {

  render() {
    let { instructions } = this.props;
    return (
      <View style={styles.container}>
        <View style={styles.top}>
          <Image source={taskyIcon} style={styles.icon} />
          <Text style={styles.logoText}>TASKY</Text>
        </View>
        <Text style={styles.instructions}>{instructions}</Text>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#93D0FF',
  },
  top: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 10,
  },
  logoText: {
    color: '#2699FB',
    textAlign: 'center',
    fontFamily: 'Arial, sans-serif',
    fontSize: 25,
    fontWeight: 'bold',
    paddingLeft: 10,
  },
  icon: {
    width: 30,
    height: 30,
  },
  instructions: {
    color: '#2699FB',
    fontFamily: 'Arial, sans-serif',
    fontSize: 16,
    fontWeight: 'bold',
    backgroundColor: '#E6F4FF',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 10,
  },
});
