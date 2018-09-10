import {Component} from '@angular/core';
import {SolarSystem} from './core/SolarSystem';
import {Router, ActivatedRoute, Params} from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  private data: any;

  constructor(private activatedRoute: ActivatedRoute) {
    this.activatedRoute.queryParams.subscribe(params => {
      let urlData = params['data'];
      // console.log(urlData);

      if (urlData) {
        let urlDataEncoded = window.atob(urlData);
        console.log(JSON.parse(urlDataEncoded));

        this.data = JSON.parse(urlDataEncoded);
        let solarSystem = new SolarSystem('solar-system', this.data);
      }
    });
  }

  dataJSON = {
    'sceneBackground': '#202020',
    'camera': {
      'fov': 80,
      'near': 1.0,
      'far': 10000.0,
      'position': {
        'x': 20,
        'y': 20,
        'z': 20,
      },
      'lookAt': {
        'x': 0,
        'y': 0,
        'z': 0,
      }
    },
    'sun': {
      'showLabel': false,
      'label': 'sun',
      'radius': 1,
      'widthSegments': 32,
      'heightSegments': 32,
      'emissive': '#ff5800',
      'emissiveIntensity': 0.5,
      'ambientLightColor': '#ffffff',
      'ambientLightIntensity': 0.3,
      'pointLightColor': '#ffffff',
      'pointLightIntensity': 1,
      'pointLightDistance': 300,
    },
    'planets': [
      {
        'radius': 0.5,
        'distance': 3.2,
        'tilt': 0.25,
        'planetColor': 'yellow',
        'lineColor': 'aqua',
        'position': 1,
        'planetName': 'mercury',
        'texture': 'mercurymap.jpg', //img name or "false"
      },
      {
        'radius': 0.6,
        'distance': 7,
        'tilt': 0.1,
        'planetColor': 'red',
        'lineColor': 'aqua',
        'position': 2,
        'planetName': 'venus',
        'texture': 'venusmap.jpg', //img name or "false"
      },
      {
        'radius': 1.0,
        'distance': 11.0,
        'tilt': 0,
        'planetColor': 'blue',
        'lineColor': 'aqua',
        'position': 6.3, //from 0 to 6.3 = 360
        'planetName': 'earth',
        'texture': 'earthmap1k.jpg', //img name or "false"
      },
      {
        'radius': 0.7,
        'distance': 14.2,
        'tilt': 0.25,
        'planetColor': 'green',
        'lineColor': 'aqua',
        'position': 0.4,
        'planetName': 'mars',
        'texture': 'mars_1k_color.jpg', //img name or "false"
      },
      {
        'radius': 0.4,
        'distance': 20,
        'tilt': 0.3,
        'planetColor': 'pink',
        'lineColor': 'aqua',
        'position': 2.6,
        'planetName': 'jupiter',
        'texture': 'jupitermap.jpg', //img name or "false"
      },
    ],
    'obiects': [
      {
        'showLine': false,
        'lineColor': '#f00',
        'startPoint': {
          'x': -10,
          'y': 0,
          'z': 0,
        },
        'endPoint': {
          'x': 0,
          'y': 10,
          'z': 10,
        },
        'additionalWaypoints': [],
        'size': 0.3,
        'objectColor': '#ff0',
        'showLabel': false,
        'label': '',
      },
      {
        'showLine': true,
        'lineColor': '#f00',
        'startPoint': {
          'x': 11,
          'y': 0,
          'z': 0,
        },
        'endPoint': {
          'x': 0,
          'y': 0.3,
          'z': -5,
        },
        'additionalWaypoints': [
          {
            'x': 0,
            'y': 0.3,
            'z': -2,
          },
          {
            'x': 0,
            'y': 0.3,
            'z': -4,
          },
        ],
        'size': 0.3,
        'objectColor': '#fff',
        'showLabel': true,
        'label': 'Apollo 11',
      },
    ],
  };
}
