import {
  WebGLRenderer,
  Object3D,
  Vector3,
  PerspectiveCamera,
  Color,
  Scene,
  CircleGeometry,
  LineBasicMaterial,
  Line,
  PointLight,
  AmbientLight,
  SphereBufferGeometry,
  MeshPhongMaterial,
  Mesh,
  TextureLoader
} from 'three';
import {CSS2DRenderer, CSS2DObject} from 'three-css2drender';

declare var require: any; //quick and dirty
const THREE = require('three');
const OrbitControls = require('three-orbit-controls')(THREE);

let scene, camera, renderer, labelRenderer;
let controls;

export class SolarSystem {
  private rootElement: any | HTMLElement | null;
  private data: any;

  constructor(rootElementId, data) {
    this.rootElement = (rootElementId && document.getElementById(rootElementId)) || document.body;

    this.data = data;

    this.init();
    this.animate(1);
  }

  prepareLabel(planetName, radius) {
    const label = document.createElement('div');
    label.className = 'label';
    label.textContent = planetName;
    label.style.marginTop = '-1em';
    label.style.color = '#FFF';
    label.style.fontFamily = 'sans-serif';
    label.style.padding = '2px';
    label.style.background = 'rgba(0,0,0,0.6)';

    const planetLabel = new CSS2DObject(label);
    planetLabel.position.set(0, radius, 0);

    return planetLabel;
  }

  createPlanet(radius, distance, tilt, planetColor, lineColor, position, planetName, texture) {
    const orbitContainer = new Object3D();
    orbitContainer.rotation.x = tilt;

    const orbit = new Object3D();

    const circleGeometry = new CircleGeometry(distance, 120);
    circleGeometry.vertices.shift();
    const line = new Line(
      circleGeometry,
      new LineBasicMaterial({color: lineColor})
    );

    line.rotation.x = Math.PI * 0.5;

    const geometry = new SphereBufferGeometry(radius, 32, 32);
    const material = new MeshPhongMaterial({color: planetColor});
    if (texture !== false) {
      material.map = new TextureLoader().load('./assets/img/' + texture);
    }

    const planet = new Mesh(geometry, material);
    planet.position.set(distance, 0.0, 0.0);

    orbit.add(line);
    orbit.add(planet);

    const planetLabel = this.prepareLabel(planetName, radius);
    planet.add(planetLabel);

    orbit.rotation.y = position;

    orbitContainer.add(orbit);
    scene.add(orbitContainer);

    return orbitContainer;
  }

  createObject(showLine, lineColor, startPoint, endPoint, additionalWaypoints, size, objectColor, showLabel, label) {
    const objectContainer = new Object3D();
    const orbit = new Object3D();

    if (showLine === true) {
      const lineGeometry = new THREE.Geometry();

      lineGeometry.vertices.push(
        new Vector3(startPoint.x, startPoint.y, startPoint.z)
      );

      if (additionalWaypoints.length > 0) {
        additionalWaypoints.forEach(function(item) {
          lineGeometry.vertices.push(
            new Vector3(item.x, item.y, item.z),
          );
        });
      }

      lineGeometry.vertices.push(
        new Vector3(endPoint.x, endPoint.y, endPoint.z)
      );

      const line = new Line(
        lineGeometry,
        new THREE.LineBasicMaterial({color: lineColor})
      );
      // line.rotation.x = Math.PI * 0.5;
      orbit.add(line);
    }

    const geometry = new SphereBufferGeometry(size, 32, 32);
    const material = new MeshPhongMaterial({color: objectColor});

    const object = new Mesh(geometry, material);
    object.position.set(endPoint.x, endPoint.y, endPoint.z);

    orbit.add(object);

    if (showLabel) {
      const objectLabel = this.prepareLabel(label, size);
      object.add(objectLabel);
    }

    objectContainer.add(orbit);
    scene.add(objectContainer);

    return objectContainer;
  }

  init() {
    scene = new Scene();
    scene.background = new Color(this.data.sceneBackground);
    // scene.background = new TextureLoader().load('./assets/img/milkyway.jpg');

    camera = new PerspectiveCamera(this.data.camera.fov, 4 / 3, this.data.camera.near, this.data.camera.far);
    camera.position.set(this.data.camera.position.x, this.data.camera.position.y, this.data.camera.position.z);
    camera.lookAt(new Vector3(this.data.camera.lookAt.x, this.data.camera.lookAt.y, this.data.camera.lookAt.z));

    renderer = new WebGLRenderer({antialias: false});

    labelRenderer = new CSS2DRenderer({antialias: false});
    labelRenderer.setSize(window.innerWidth, window.innerHeight);
    labelRenderer.domElement.style.position = 'absolute';
    labelRenderer.domElement.style.top = 0;

    controls = new OrbitControls(camera);

    const ambientLight = new AmbientLight(this.data.sun.ambientLightColor, this.data.sun.ambientLightIntensity);
    scene.add(ambientLight);

    const solar = new Mesh(
      new SphereBufferGeometry(this.data.sun.radius, this.data.sun.widthSegments, this.data.sun.heightSegments),
      new MeshPhongMaterial({
        emissive: this.data.sun.emissive,
        emissiveIntensity: this.data.sun.emissiveIntensity,
        map: new TextureLoader().load('./assets/img/sunmap.jpg')
      })
    );

    const pointLight = new PointLight(this.data.sun.pointLightColor, this.data.sun.pointLightIntensity, this.data.sun.pointLightDistance);

    solar.add(pointLight);
    scene.add(solar);

    if (this.data.sun.showLabel === true) {
      const sunLabel = this.prepareLabel(this.data.sun.label, this.data.sun.radius);
      solar.add(sunLabel);
    }

    this.data.planets.forEach(function (item) {
      this.createPlanet(item.radius, item.distance, item.tilt, item.planetColor, item.lineColor, item.position, item.planetName, item.texture);
    }.bind(this));

    this.data.obiects.forEach(function (item) {
      this.createObject(item.showLine, item.lineColor, item.startPoint, item.endPoint, item.additionalWaypoints, item.size, item.objectColor, item.showLabel, item.label);
    }.bind(this));

    window.addEventListener('resize', this.onWindowResize, false);
    this.onWindowResize();

    document.body.appendChild(renderer.domElement);
    document.body.appendChild(labelRenderer.domElement);
  }

  onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
    labelRenderer.setSize(window.innerWidth, window.innerHeight);
  }

  animate(time) {
    controls.update();

    renderer.render(scene, camera);
    labelRenderer.render(scene, camera);
    window.requestAnimationFrame(() => this.animate(time));
  }

}
